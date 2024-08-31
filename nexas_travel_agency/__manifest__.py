{
    "name":"Nexas Travel Agency",
    "author":"Target Integration",
    "description":"This is a travel agency management system",
    'version': '17.0.1.1',
    'depends': ['base','account','mail','product'],
    'data':[
        "security/travel_security.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/travel_itinerary_views.xml",
        "views/travel_document_views.xml",
        "views/travel_booking_views.xml",
        "views/travel_trip_views.xml",
        "views/travel_report_views.xml",
        "views/travel_supplier_views.xml",
        "views/travel_product_views.xml",
        "views/travel_agency_views.xml",
        "views/menus.xml",
        "data/travel.trip.csv",
        "data/travel_trip_data.xml"
        
    ],
    "assets":{
        'web.assets_backend':[
            "nexas_travel_agency/static/src/css/custom_styles.css"
        ],
    },
    'license': 'LGPL-3',
}