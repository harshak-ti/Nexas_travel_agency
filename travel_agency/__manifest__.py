{
   "name":"Travel Agency",
    "author":"Target Integration",
    "description":"This is a travel agency management system",
    'version': '17.0.1.2',
    'depends':['base','sale','product','mail'],
    "data":[
        "security/ir.model.access.csv",
        "views/trip_booking_views.xml",
        "views/trip_inherit_views.xml",
        "views/itinerary_inherit_views.xml",
        "views/travel_booking_confirm_wizard_views.xml",
        "views/menus.xml"
    ],
    "license":"LGPL-3"
}