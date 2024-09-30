{
    "name":"Nexas Travel Agency",
    "author":"Target Integration",
    "description":"This is a travel agency management system",
    'version': '17.0.1.1',
    'depends': ['base','account','mail','product','web','sale','professional_templates'],
    'data':[
        "security/travel_security.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "data/mail_template.xml",
        "views/travel_itinerary_views.xml",
        "views/travel_document_views.xml",
        "views/travel_booking_views.xml",
        "views/travel_trip_views.xml",
        "views/travel_report_views.xml",
        "views/travel_supplier_views.xml",
        "views/travel_product_views.xml",
        "views/travel_agency_views.xml",
        "views/travel_agency_driver_view.xml",
        "views/travel_agency_vehicles_views.xml",
        "views/res_partner_views.xml",
        "views/sale_order_inherit_views.xml",
        "views/template_inherit.xml",
        "views/report_travel_trip.xml",
        "views/report_travel_booking.xml",
        "views/template.xml",
        # "report/driver_idcard_template.xml",
        # "views/report_template.xml",
        "views/menus.xml",
        "data/travel_trip_data.xml",
        "data/travel_agency_vehicles.xml",
        "data/travel_agency_drivers.xml"
       
        
    ],
    "assets":{
        'web.assets_backend':[
         
            "static/src/js/demo.js",
            "static/src/js/custom_button.js",
      "static/src/js/confirm_booking.js",
      "static/src/xml/demo.xml",
            "nexas_travel_agency/static/src/css/custom_styles.css",
          'nexas_travel_agency/static/src/css/trip_view.css',
        ],
        'web.assets_frontend': [
        ],
    },
    'license': 'LGPL-3',
}