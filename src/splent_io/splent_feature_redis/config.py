"""
Redis infrastructure configuration.

Provides the Redis connection URL. Session management is handled by
splent_feature_session_redis (separate feature).
"""

import os


def inject_config(app):
    redis_url = os.getenv("REDIS_URL", "redis://redis:6379")

    app.config.update(
        {
            "REDIS_URL": redis_url,
        }
    )
