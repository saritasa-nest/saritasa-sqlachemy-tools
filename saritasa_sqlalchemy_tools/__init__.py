import contextlib

from .models import (
    BaseIDModel,
    BaseModel,
    BaseModelT,
    BaseSoftDeleteModel,
    BaseSoftDeleteModelT,
    BaseTimeStampedModel,
    FieldEnumT,
    ModelAttribute,
    ModelAttributeSequence,
    ModelType,
    SelectStatement,
    SoftDeleteBaseIDModel,
    SoftDeleteMixin,
    SQLAlchemyModel,
    TimeStampedBaseIDModel,
    TimeStampedMixin,
)
from .repositories import (
    Annotation,
    AnnotationSequence,
    BaseRepository,
    BaseRepositoryT,
    BaseSoftDeleteRepository,
    ComparisonOperator,
    Filter,
    FilterType,
    LazyLoaded,
    LazyLoadedSequence,
    OrderingClause,
    OrderingClauses,
    OrderingEnum,
    OrderingEnumMeta,
    SQLWhereFilter,
    SubQueryReturnT,
    WhereFilter,
    WhereFilters,
    transform_search_filter,
)
from .session import (
    Session,
    SessionContextManager,
    SessionContextManagerGetter,
    SessionFactory,
    get_async_db_session,
    get_async_engine,
    get_async_session_factory,
    set_search_path,
)

with contextlib.suppress(ImportError):
    from .testing import (
        AsyncSQLAlchemyModelFactory,
        AsyncSQLAlchemyOptions,
        DateRangeFactory,
    )

with contextlib.suppress(ImportError):
    from .alembic import AlembicMigrations

with contextlib.suppress(ImportError):
    from .schema import (
        ModelAutoSchema,
        ModelAutoSchemaError,
        ModelAutoSchemaT,
        OpenAPIDocsEnumMixin,
        PostgresDateRange,
        PostgresRange,
        PostgresRangeTypeT,
    )

__all__ = (
    "AlembicMigrations",
    "AsyncSQLAlchemyModelFactory",
    "AsyncSQLAlchemyOptions",
    "DateRangeFactory",
    "Session",
    "SessionContextManager",
    "SessionContextManagerGetter",
    "SessionFactory",
    "get_async_db_session",
    "get_async_engine",
    "get_async_session_factory",
    "set_search_path",
    "Annotation",
    "AnnotationSequence",
    "BaseRepository",
    "BaseRepositoryT",
    "BaseSoftDeleteRepository",
    "ComparisonOperator",
    "Filter",
    "FilterType",
    "LazyLoaded",
    "LazyLoadedSequence",
    "OrderingClause",
    "OrderingClauses",
    "OrderingEnum",
    "OrderingEnumMeta",
    "SQLWhereFilter",
    "SubQueryReturnT",
    "WhereFilter",
    "WhereFilters",
    "transform_search_filter",
    "BaseIDModel",
    "BaseModel",
    "BaseModelT",
    "BaseSoftDeleteModel",
    "BaseSoftDeleteModelT",
    "BaseTimeStampedModel",
    "FieldEnumT",
    "ModelAttribute",
    "ModelAttributeSequence",
    "ModelType",
    "SelectStatement",
    "SoftDeleteBaseIDModel",
    "SoftDeleteMixin",
    "SQLAlchemyModel",
    "TimeStampedBaseIDModel",
    "TimeStampedMixin",
    "ModelAutoSchema",
    "ModelAutoSchemaError",
    "ModelAutoSchemaT",
    "PostgresRange",
    "PostgresRangeTypeT",
    "PostgresDateRange",
    "OpenAPIDocsEnumMixin",
)
