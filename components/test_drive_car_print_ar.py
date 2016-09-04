# -*- coding: utf-8 -*-
from meya import Component


class HelloWorld(Component):

    def start(self):
        carsar = [
                {'caridentar': 'a_class_sedan','label': 'الفئة - A'},
                {'caridentar': 'c_class_sedan','label': 'الفئة - C سيدان'},
                {'caridentar': 'c_class_coupe','label': 'الفئة - C كوبيه'},
                {'caridentar': 'cla_coupe','label': 'CLA كوبيه'},
                {'caridentar': 'cls_coupe','label': 'CLS كوبيه'},
                {'caridentar': 'e_class_sedan','label': 'الفئة - E سيدان'},
                {'caridentar': 'e_class_coupe','label': 'الفئة - E كوبيه'},
                {'caridentar': 'e_class_cabriolet','label': 'الفئة - E كابريوليه'},
                {'caridentar': 's_class_sedan','label': 'الفئة - S سيدان'},
                {'caridentar': 's_class_coupe','label': 'الفئة - S كوبيه'},
                {'caridentar': 'g_class_suv','label': 'الفئة - G'},
                {'caridentar': 'gla_suv','label': 'GLA'},
                {'caridentar': 'glc_suv','label': 'GLC'},
                {'caridentar': 'gle_suv','label': 'GLE'},
                {'caridentar': 'gle_coupe','label': 'GLE كوبيه'},
                {'caridentar': 'gls_suv','label': 'GLS'},
                {'caridentar': 'amg_gt','label': 'AMG-GT'},
                {'caridentar': 'sl','label': 'SL'},
                {'caridentar': 'slc','label': 'SLC'},
                {'caridentar': 'v_class','label': 'لفئة - V'}
               ]
        
        for car in carsar:
            #print car
            self.db.table('carsar').add(car)
        car_query = self.db.table('carsar').filter(caridentar=self.db.flow.get('test_drive_car_confirmed'))
        car_label = "car"
        #car_querys = car_query.items()
        #for q in car_query:
        #    car_label = q['label']
        if car_query[0]['label'] and isinstance(car_query[0]['label'], (basestring, str, unicode)):
            car_label = car_query[0]['label']
        print car_label
        self.db.user.set('test_drive_car_name', car_label)
            
        #car_label = car_query.label
            
        text = "أختيار عظيم! لقد قمت بإختيار ‎{}".format(
            car_label
        )
        message = self.create_message(text=text)
        #Replace <car Model> with value of 
        
        return self.respond(message=message, action="next")
