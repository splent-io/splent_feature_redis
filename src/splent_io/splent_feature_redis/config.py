import os
import redis


def inject_config(app):
    redis_url = os.getenv("REDIS_URL", "redis://redis:6379")

    app.config.update(
        {
            "SESSION_TYPE": "redis",
            "SESSION_PERMANENT": False,
            "REDIS_URL": redis_url,
            "SESSION_REDIS": redis.from_url(redis_url),
        }
    )
