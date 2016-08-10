# -*- coding: utf-8 -*-
from meya import Component


class HelloWorld(Component):

    def start(self):
        cars = [
                {'carident': 'a_class_sedan','label': 'A-Class'},
                {'carident': 'c_class_sedan','label': 'C-Class Sedan'},
                {'carident': 'c_class_coupe','label': 'C-Class Coupé'},
                {'carident': 'cla_coupe','label': 'CLA Coupé'},
                {'carident': 'cls_coupe','label': 'CLS Coupé'},
                {'carident': 'e_class_sedan','label': 'E-Class Sedan'},
                {'carident': 'e_class_coupe','label': 'E-Class Coupé'},
                {'carident': 'e_class_cabriolet','label': 'E-Class Cabriolet'},
                {'carident': 's_class_sedan','label': 'S-Class Sedan'},
                {'carident': 's_class_coupe','label': 'S-Class Coupé'},
                {'carident': 'g_class_suv','label': 'G-Class'},
                {'carident': 'gla_suv','label': 'GLA'},
                {'carident': 'glc_suv','label': 'GLC'},
                {'carident': 'gle_suv','label': 'GLE'},
                {'carident': 'gle_coupe','label': 'GLE Coupé'},
                {'carident': 'gls_suv','label': 'GLS'},
                {'carident': 'amg_gt','label': 'AMG-GT'},
                {'carident': 'sl','label': 'SL'},
                {'carident': 'slc','label': 'SLC'},
                {'carident': 'v_class','label': 'V-Class'}
               ]
        
        for car in cars:
            #print car
            self.db.table('cars').add(car)
        car_query = self.db.table('cars').filter(carident=self.db.flow.get('test_drive_car_confirmed'))
        car_label = "car"
        #car_querys = car_query.items()
        #for q in car_query:
        #    car_label = q['label']
        if car_query[0]['label'] and isinstance(car_query[0]['label'], (basestring, str, unicode)):
            car_label = car_query[0]['label']
        print car_label
        self.db.user.set('test_drive_car_name', car_label)
            
        #car_label = car_query.label
            
        text = "You’ve chosen the {}. Great choice!".format(
            car_label
        )
        message = self.create_message(text=text)
        #Replace <car Model> with value of 
        
        return self.respond(message=message, action="next")
