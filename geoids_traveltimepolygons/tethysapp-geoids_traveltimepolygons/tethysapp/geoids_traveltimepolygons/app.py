from tethys_sdk.base import TethysAppBase, url_map_maker


class geoids_traveltimepolygons(TethysAppBase):
    """
    Tethys app class for Travel Time Distance Map App.
    """

    name = 'Travel Time Polygons'
    index = 'geoids_traveltimepolygons:home'
    icon = 'geoids_traveltimepolygons/images/car.jpg'
    package = 'geoids_traveltimepolygons'
    root_url = 'geoids_traveltimepolygons'
    color = '#800000'
    description = 'This app shows how far vehicles can travel along any route through a road network in a given amount of time.'
    tags = '&quot;Transportation&quot;,&quot;Travel Times&quot;,&quot;Road Network&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='geoids_traveltimepolygons',
                controller='geoids_traveltimepolygons.controllers.home'
            ),
            UrlMap(
                name='map',
                url='geoids_traveltimepolygons/map',
                controller='geoids_traveltimepolygons.controllers.map'
            ),
            UrlMap(
                name='proposal',
                url='geoids_traveltimepolygons/proposal',
                controller='geoids_traveltimepolygons.controllers.proposal'
            ),
            UrlMap(
                name='design',
                url='geoids_traveltimepolygons/design',
                controller='geoids_traveltimepolygons.controllers.design'
            ),
        )

        return url_maps

