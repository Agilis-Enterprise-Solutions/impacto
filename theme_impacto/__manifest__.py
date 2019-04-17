# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Theme Impacto',
    'summary': 'Html5 Responsive E-Commerce And Multi-Purpose theme',
    'category': 'Theme/Ecommerce',
    'author': 'Adventumweb',
    'sequence': 1,
    'version': '1.2',
	'license' : 'OPL-1',
    'depends': [
        'website',
        'website_crm',
        'web',
        'theme_common',
        'auth_signup',
        'website_sale',
        'website_blog',
        'website_event'],
    'data': [   
        'views/customize_modal.xml',
        'views/assets.xml',   
		'views/blog.xml',
		'views/shop.xml',
        'views/page_login.xml',
        'views/page_eventlist.xml',
        'views/page_contact.xml',
        'views/page_homepage.xml',
		'views/page_home-agency.xml',
        'views/page_home-creative-bussiness.xml',
		'views/page_home-corporate.xml',
		'views/page_home-construction.xml',
		'views/page_home-medical.xml',
        'views/page_home-gym.xml',
		'views/page_home-app.xml',
		'views/page_home-education.xml',
        'views/page_home-restaurant.xml',
		'views/page_home-shop.xml',
        'views/page_home-shop-shoes.xml',
        'views/page_home-shop-furniture.xml',
		'views/page_home-fashion.xml',
		'views/page_home-goggle.xml',
		'views/page_home-industry.xml',
		'views/page_home-solar.xml',
		'views/page_home-coffee.xml',
		'views/page_home-drone.xml',
		'views/page_home-landscaping.xml',
		'views/page_home-transport.xml',
		'views/page_home-architecture.xml',
		'views/page_about-01.xml',
        'views/page_about-02.xml',
        'views/page_about-03.xml',
		'views/page_service-01.xml',
        'views/page_service-02.xml',
		'views/page_service-03.xml',
        'views/page_faq.xml',        
		'views/page_team.xml',
		'views/page_portfolio.xml',
		'views/snippets.xml',
        'views/snippets_option.xml',
		'views/header.xml',
        'views/footer.xml'
    ],
    'images': [
      'static/description/impacto.jpg',
 	  'static/description/impacto_screenshot.jpg'
    ],
    'price': '149',
    'currency':'EUR',
    'live_test_url':'http://198.251.72.29/',
	'installable': True,
    'application': True,
}
