# Schema Guide

Registry files are JSON objects with a top-level `nodes` or `edges` array.

Node essentials: `id`, `type`, `title`, `summary`, `source_system`, `status`, `maturity`, `owner_domain`, `authoritative_for`, `not_authoritative_for`, `why_read`, `related_tags`, `last_verified`, `reopen_priority`.

Edge essentials: `id`, `from`, `to`, `relation`, `description`, `confidence`, `status`.

The edge `description` is not decoration. It preserves the accumulated understanding of **why** the connection exists.
