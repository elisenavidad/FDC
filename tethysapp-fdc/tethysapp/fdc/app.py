from tethys_sdk.base import TethysAppBase, url_map_maker


class Fdc(TethysAppBase):
    """
    Tethys app class for FDC.
    """

    name = 'Flow Duration Curve'
    index = 'fdc:home'
    icon = 'fdc/images/icon.gif'
    package = 'fdc'
    root_url = 'fdc'
    color = '#1e62ce'
    description = 'Calculate the potential reservoir storage capacity and flow-duration curve in the Dominican Republic given a dam height and a curve number.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='fdc',
                           controller='fdc.controllers.home'),
                    UrlMap(name='results',
                        url='results',
                        controller='fdc.controllers.results'),

                    )

        return url_maps