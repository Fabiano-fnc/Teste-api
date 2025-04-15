from .usuario import router as usuario_router
from .filme import router as filme_router
from .review import router as review_router

__all__ = ["usuario_router", "filme_router", "review_router"]