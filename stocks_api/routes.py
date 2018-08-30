from pyramid_restful.routers import ViewSetRouter
from .views.stock import StockAPIView
from .views.portfolio import PortfolioAPIView
from .views.auth import AuthAPIView
from .views.company import CompanyAPIView


def includeme(config):
    """Route adding and configuration
    """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('lookup', 'api/v1/lookup/{symbol}')

    router = ViewSetRouter(config)
    router.register('api/v1/auth/{auth}', AuthAPIView, 'auth')
    router.register('api/v1/portfolio', PortfolioAPIView, 'portfolio', permission='admin')
    router.register('api/v1/stock', StockAPIView, 'stock', permission='admin')
    router.register('api/v1/company', CompanyAPIView, 'company', permission='view')
