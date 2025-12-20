from sqlalchemy import (
    MetaData, Table, Column, Text, Enum,
    DateTime, Numeric, ForeignKey, CheckConstraint, Index
)
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from app.enums import PackageStatus, EventType
import uuid

metadata = MetaData()

package_table = Table(
    'packages',
    metadata,
    Column('package_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('tracking_code', Text, unique=True, nullable=False),
    Column('description', Text, nullable=False),
    Column('destination', Text, nullable=False),
    Column('weight_kg', Numeric, CheckConstraint('weight_kg > 0'), nullable=False),
    Column('status', Enum(PackageStatus), nullable=False),
    Column('created_at', DateTime(timezone=True), server_default=func.now(), nullable=False),
    Column('updated_at', DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False),
    Column('last_scan_at', DateTime(timezone=True), nullable=True),   
)

Index("ix_packages_status_destination", package_table.c.status, package_table.c.destination)
Index("ix_packages_last_scan_at", package_table.c.last_scan_at)

scan_events_table = Table(
    'scan_events',
    metadata,
    Column('event_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('package_id', UUID(as_uuid=True), ForeignKey('packages.package_id'), nullable=False),
    Column('occurred_at', DateTime(timezone=True), server_default=func.now(), nullable=False),
    Column('event_type', Enum(EventType), nullable=False),
    Column('location', Text, nullable=False),
    Column('meta', JSONB, nullable=True),
    )

Index("ix_scan_events_package_id_occurred_at", scan_events_table.c.package_id, scan_events_table.c.occurred_at)