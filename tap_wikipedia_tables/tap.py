"""wikipedia tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_wikipedia_tables.streams import (
    wikipediaStream,
    UsersStream,
    GroupsStream,
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    UsersStream,
    GroupsStream,
]


class Tapwikipedia(Tap):
    """wikipedia tap class."""
    name = "tap-wikipedia-tables"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        # th.Property(
        #     "pages",
        #     th.ArrayType(th.StringType),
        #     required=True,
        #     description="Page names"
        # ),
        th.Property(
            "page",
            th.StringType,
            required=True,
            description="Page name"
        ),        
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
