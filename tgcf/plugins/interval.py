"""Plugin for interval message posting."""

import asyncio
import logging
from typing import Dict, Any

from telethon.tl.custom.message import Message

from tgcf.plugins import TgcfMessage, TgcfPlugin


class TgcfInterval(TgcfPlugin):
    """Plugin to send interval messages."""

    id_ = "interval"

    def __init__(self, data: Dict[str, Any]) -> None:
        super().__init__(data)
        self.interval_tasks = {}

    async def __ainit__(self) -> None:
        """Initialize interval tasks."""
        pass

    async def start_interval_posting(self, forward_config, client):
        """Start interval posting for a specific forward."""
        if not forward_config.enable_interval_posting:
            return

        forward_id = f"{forward_config.source}_{forward_config.con_name}"
        
        if forward_id in self.interval_tasks:
            # Stop existing task
            self.interval_tasks[forward_id].cancel()
        
        # Start new interval task
        task = asyncio.create_task(
            self._interval_posting_loop(forward_config, client, forward_id)
        )
        self.interval_tasks[forward_id] = task
        logging.info(f"Started interval posting for {forward_id}")

    async def stop_interval_posting(self, forward_config):
        """Stop interval posting for a specific forward."""
        forward_id = f"{forward_config.source}_{forward_config.con_name}"
        
        if forward_id in self.interval_tasks:
            self.interval_tasks[forward_id].cancel()
            del self.interval_tasks[forward_id]
            logging.info(f"Stopped interval posting for {forward_id}")

    async def _interval_posting_loop(self, forward_config, client, forward_id):
        """Main loop for interval posting."""
        try:
            while True:
                # Send message to all destinations
                for dest in forward_config.dest:
                    try:
                        await client.send_message(
                            dest, forward_config.interval_message
                        )
                        logging.info(f"Sent interval message to {dest}")
                    except Exception as e:
                        logging.error(f"Failed to send interval message to {dest}: {e}")
                
                # Wait for next interval
                await asyncio.sleep(forward_config.interval_seconds)
                
        except asyncio.CancelledError:
            logging.info(f"Interval posting cancelled for {forward_id}")
        except Exception as e:
            logging.error(f"Error in interval posting loop for {forward_id}: {e}")

    def modify(self, tm: TgcfMessage) -> TgcfMessage:
        """Modify the message (not used for interval posting)."""
        return tm
