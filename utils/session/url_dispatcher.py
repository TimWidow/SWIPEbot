# Contains all the relative paths for SwipeRestApi
REL_URLS = {
    # ADMIN
    'admin_login': 'api/admin/login/',
    'users': 'api/admin/users/',
    'promotions': 'api/admin/promotion/',
    'subscription': 'api/admin/users/{pk}/subscription/',
    # APARTMENTS
    'apartments': 'api/user/apartments/',
    'booking_apart': 'api/apartments/{apart_pk}/booking/',
    'requests': 'api/user/requests/',
    # COMPLAINTS
    'complaints': 'api/complaints/',
    'complaints_admin': 'api/admin/complaints',
    # FAVORITES
    'favorites': 'api/user/favorites_posts/',
    # Like/Dislike
    'like_dislike': 'api/user/like_dislike/{pk}/',
    # FILTERS
    'filters': 'api/user_filters/',
    # USERS
    'login': 'api/login/',
    'posts': 'api/user/posts/',
    'user/promotions': 'api/user/promotion/{pk}',
    'promotion_types': 'api/user/promotion_type/',
    # USER HOUSES
    'houses': 'api/user/houses/',
    'blocks': 'api/user/blocks/',
    'buildings': 'api/user/buildings/',
    'sections': 'api/user/sections/',
    'floors': 'api/user/floors/',
    'standpipes': 'api/user/standpipes/',
    # PUBLIC
    'posts_public': 'api/posts/',
    'houses_public': 'api/houses/',
    'apartments_public': 'api/apartments/',
    # NEWS
    'news': 'api/news/',
    # DOCUMENTS
    'documents': 'api/documents/',

}
