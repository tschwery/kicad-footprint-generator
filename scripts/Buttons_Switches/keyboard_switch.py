#!/usr/bin/env python

import sys
import os
import math

sys.path.append(os.path.join(sys.path[0],"..","..","kicad_mod")) # load kicad_mod path
sys.path.append(os.path.join(sys.path[0],"..",".."))

from KicadModTree import *

unit_width = 9.525

keysizes = [
    {
        'Name': '1.00u'
       ,'Size': 1.00
    }
   ,{
        'Name': '1.25u'
       ,'Size': 1.25
    }
   ,{
        'Name': '1.50u'
       ,'Size': 1.50
    }
   ,{
        'Name': '1.75u'
       ,'Size': 1.75
    }
   ,{
        'Name': '2.00u'
       ,'Size': 2.00
       ,'Stab_width': 11.90
    }
   ,{
        'Name': '2.25u'
       ,'Size': 2.25
       ,'Stab_width': 11.90
    }
   ,{
        'Name': '2.75u'
       ,'Size': 2.75
       ,'Stab_width': 11.90
    }
   ,{
        'Name': '6.25u'
       ,'Size': 6.25
       ,'Stab_width': 50.00
    }
   ,{
        'Name': 'ISOEnter'
       ,'Size': 2.00
       ,'Stab_width': 11.90
       ,'Key_rotation': 270
       ,'Segments': [
                    [[-11.90625,  19.05], [-11.90625,   0.00]]
                   ,[[-16.66875, -19.05], [ 11.90625, -19.05]]
                   ,[[ 11.90625, -19.05], [ 11.90625,  19.05]]
                   ,[[ 11.90625,  19.05], [-11.90625,  19.05]]
                   ,[[-16.66875,   0.00], [-16.66875, -19.05]]
                   ,[[-11.90625,   0.00], [-16.66875,   0.00]]
                   ]
   }
]

layers = {
    'F.Fab': {
        'Width': 0.1
    }
   ,'F.CrtYd': {
        'Width': 0.05
    }
   ,'Dwgs.User': {
        'Width': 0.15
    }
   ,'F.SilkS': {
        'Width': 0.12
    }
}

cherry_switch_plate = {
    'Center' :     [-2.54,  5.08 ]
   ,'T.Reference': [-2.54, -2.794]
   ,'T.Value':     [-2.54, 12.954]
   ,'T.User':      [-2.54, -2.794]
   ,'F.Fab':   { 'Comparison': { 'Layer': 'F.SilkS', 'Difference': [- 0.635,- 0.635 ] } }
   ,'F.CrtYd': { 'Comparison': { 'Layer': 'F.SilkS', 'Difference': [- 0.385,- 0.385 ] } }
   ,'F.SilkS': { 'Limits': [ 6.985, 6.985] }
   ,'H.Pads': [
        [  0.00, 0.00]
       ,[- 6.35, 2.54]
   ]
   ,'H.Stabs' : {
        'All': [
            [- 2.54,   5.08, 4.00]
        ]
    }
}

gateron_switch_smd_plate = {
    'Center' :     [-2.54,  5.08 ]
   ,'T.Reference': [-2.54, -2.794]
   ,'T.Value':     [-2.54, 12.954]
   ,'T.User':      [-2.54, -2.794]
   ,'F.Fab':   { 'Comparison': { 'Layer': 'F.SilkS', 'Difference': [- 0.635,- 0.635 ] } }
   ,'F.CrtYd': { 'Comparison': { 'Layer': 'F.SilkS', 'Difference': [- 0.385,- 0.385 ] } }
   ,'F.SilkS': { 'Points': [
                                [- 9.525,- 1.905], [  4.445,- 1.905],
                                [  4.445, 12.065], [  1.460, 12.065],
                                [  1.460, 10.005], [- 6.540, 10.005],
                                [- 6.540, 12.065], [- 9.525, 12.065]
                           ]
    }
   ,'H.Pads': [
        [  0.00, 0.00]
       ,[- 6.35, 2.54]
   ]
   ,'H.Stabs' : {
        'All': [
            [- 2.54,   5.08, 4.00]
        ]
    }
}

cherry_switch_pcb = {
    'Center' :     [-2.54,  5.08 ]
   ,'T.Reference': [-2.54, -2.794]
   ,'T.Value':     [-2.54, 12.954]
   ,'T.User':      [-2.54, -2.794]
   ,'F.Fab':   { 'Comparison': { 'Layer': 'F.SilkS', 'Difference': [- 0.635,- 0.635 ] } }
   ,'F.CrtYd': { 'Comparison': { 'Layer': 'F.SilkS', 'Difference': [- 0.385,- 0.385 ] } }
   ,'F.SilkS': { 'Limits': [ 6.985, 6.985] }
   ,'H.Pads': [
        [  0.00, 0.00]
       ,[- 6.35, 2.54]
   ]
   ,'H.Stabs' : {
        'All' : [
            [- 2.54,   5.08, 4.00],
            [- 7.62,   5.08, 1.70], [  2.54,   5.08, 1.70]
        ]
       ,'2.00u' : [
            [- 2.54,   5.08, 4.00],
            [- 7.62,   5.08, 1.70], [  2.54,   5.08, 1.70],
            [  9.36,  13.32, 4.00], [-14.44,  13.32, 4.00],
            [-14.44, - 1.92, 3.05], [  9.36, - 1.92, 3.05]
        ]
       ,'2.25u' : [
            [- 2.54,   5.08, 4.00],
            [- 7.62,   5.08, 1.70], [  2.54,   5.08, 1.70],
            [  9.36,  13.32, 4.00], [-14.44,  13.32, 4.00],
            [-14.44, - 1.92, 3.05], [  9.36, - 1.92, 3.05]
        ]
       ,'2.50u' : [
            [- 2.54,   5.08, 4.00],
            [- 7.62,   5.08, 1.70], [  2.54,   5.08, 1.70],
            [  9.36,  13.32, 4.00], [-14.44,  13.32, 4.00],
            [-14.44, - 1.92, 3.05], [  9.36, - 1.92, 3.05]
        ]
       ,'2.75u' : [
            [- 2.54,   5.08, 4.00],
            [- 7.62,   5.08, 1.70], [  2.54,   5.08, 1.70],
            [  9.36,  13.32, 4.00], [-14.44,  13.32, 4.00],
            [-14.44, - 1.92, 3.05], [  9.36, - 1.92, 3.05]
        ]
       ,'6.25u' : [
            [- 2.54,   5.08, 4.00],
            [- 7.62,   5.08, 1.70], [  2.54,   5.08, 1.70],
            [-50.00,  13.32, 4.00], [ 50.00,  13.32, 4.00],
            [-50.00, - 1.92, 3.05], [ 50.00, - 1.92, 3.05]
        ]
       ,'ISOEnter' : [
            [- 2.54,   5.08, 4.00],
            [- 7.62,   5.08, 1.70], [  2.54,   5.08, 1.70],
            [  5.70, - 6.82, 4.00], [  5.70,  16.98, 4.00],
            [- 9.54,  16.98, 3.05], [- 9.54, - 6.82, 3.05]
        ]
   }
}

matias_switch = {
    'Center' :     [- 2.50,  4.50 ]
   ,'T.Reference': [- 2.50,- 3.75 ]
   ,'T.Value':     [- 2.50, 12.75 ]
   ,'T.User':      [- 2.50,  4.50 ]
   ,'F.Fab':   { 'Comparison': { 'Layer': 'F.SilkS', 'Difference': [- 0.25,- 0.25 ] } }
   ,'F.CrtYd': { 'Comparison': { 'Layer': 'F.SilkS', 'Difference': [  0.00,  0.00 ] } }
   ,'F.SilkS': { 'Limits': [ 8.85,  7.25 ] }
   ,'H.Pads' : [
        [ 0.00, 0.00]
       ,[-5.00, 0.50]
   ]
}

def rotate_point(angle, center):
    rangle = math.radians(angle)
    def rotate_pre(point):
        x0 = point[0] - center[0]
        y0 = point[1] - center[1]
        return [
            x0 * math.cos(rangle) - y0 * math.sin(rangle) + center[0]
           ,y0 * math.cos(rangle) + x0 * math.sin(rangle) + center[1]
        ]
    return rotate_pre

def center_point(center):
    def center_pre(point):
        x0 = point[0] + center[0]
        y0 = point[1] + center[1]
        return [x0, y0]
    return center_pre

def list_rotate(l, n):
    return l[-n:] + l[:-n]

def get_layer_points(layer, data):
    center = data['Center']

    if 'Limits' in data[layer]:
        limits = data[layer]['Limits']
        tl = [- limits[0], - limits[1]]
        tr = [- limits[0], + limits[1]]
        bl = [+ limits[0], - limits[1]]
        br = [+ limits[0], + limits[1]]
        points = list(map(center_point(center),[tl, bl, br, tr]))
    elif 'Comparison' in data[layer]:
        com_layer = data[layer]['Comparison']['Layer']
        com_diff = data[layer]['Comparison']['Difference']
        
        com_points = get_layer_points(com_layer, data)
        points = []
        for idx, point in enumerate(com_points):
            prev_point = com_points[idx - 1]
            next_point = com_points[idx + 1] if (idx + 1) < len(com_points) else com_points[0]
            x_dir = prev_point[0] - point[0] + next_point[0] - point[0]
            y_dir = prev_point[1] - point[1] + next_point[1] - point[1]
            
            points.append([point[0] + math.copysign(com_diff[0], x_dir), point[1] + math.copysign(com_diff[1], y_dir)])
    else:
        points = data[layer]['Points']
    
    return points

def generate_switch_layer(kicad_mod, layer, size, data):
    points = get_layer_points(layer, data)
    
    if 'Key_rotation' in size:
        center = data['Center']
        size_rotation = size['Key_rotation']
        points = list(map(rotate_point(size_rotation, center), points))
    
    points_start = points.copy()
    points_end = list_rotate(points.copy(), -1)
    
    layer_info = layers[layer]
    for segment in zip(points_start, points_end):
        kicad_mod.append(Line(start=segment[0], end=segment[1], layer=layer, width=layer_info['Width']))

def generate_keysize_layer(kicad_mod, layer, size, data):
    center = data['Center']
    layer_info = layers[layer];

    if 'Segments' in size:
        segments = size['Segments']
    else:
        tl = [- (unit_width * size['Size']), - (unit_width)]
        tr = [- (unit_width * size['Size']), + (unit_width)]
        bl = [+ (unit_width * size['Size']), - (unit_width)]
        br = [+ (unit_width * size['Size']), + (unit_width)]

        points = [tl, bl, br, tr]
        points_start = points.copy()
        points_end = list_rotate(points.copy(), 1)
        
        segments = list(zip(points_start, points_end))
    
    center_pre = center_point(center)
    for segment in segments:
        kicad_mod.append(Line(start=center_pre(segment[0]), end=center_pre(segment[1]), layer=layer, width=layer_info['Width']))


def generate_pads_layer(kicad_mod, layer, size, data):
    pads = data['H.Pads']
    center = data['Center']

    for idx, pad in enumerate(pads):
        x = pad[0]
        y = pad[1]
        kicad_mod.append(Pad(number=(idx+1)
                             ,type=Pad.TYPE_THT
                             ,shape=Pad.SHAPE_CIRCLE
                             ,at=[x, y]
                             ,size=[2.2, 2.2]
                             ,drill=1.5
                             ,layers=['*.Cu', '*.Mask']))

def generate_stabs_layer(kicad_mod, layer, size, data):
    center = data['Center']
    size_name = size['Name']
    
    if 'H.Stabs' not in data:
        return

    stab_data = data['H.Stabs']
    
    if size_name not in stab_data and 'All' not in stab_data:
        return
    
    if size_name not in stab_data:
        pads = stab_data['All']
    else:
        pads = stab_data[size_name]
    
    for pad in pads:
        x = pad[0]
        y = pad[1]
        d = pad[2]
        kicad_mod.append(Pad(type=Pad.TYPE_NPTH
                            ,shape=Pad.SHAPE_CIRCLE
                            ,at=[x, y]
                            ,size=[d, d]
                            ,drill=d
                            ,layers=['*.Cu', '*.Mask']))

def gen_key(name_pattern, desc_pattern, tags_pattern, data):
    for size in keysizes:
        size_name = size['Name']
        footprint_name = name_pattern.format(size=size_name)
        
        # init kicad footprint
        kicad_mod = Footprint(footprint_name)
        kicad_mod.setDescription(desc_pattern.format(size=size_name))
        kicad_mod.setTags(tags_pattern.format(size=size_name))

        # set general values
        kicad_mod.append(Text(type='reference', text='REF**', at=data['T.Reference'], layer='F.SilkS'))
        kicad_mod.append(Text(type='value', text=footprint_name, at=data['T.Value'], layer='F.Fab'))

        if 'T.User' in data:
            kicad_mod.append(Text(type='user', text='%R', at=data['T.User'], layer='F.Fab'))

        for layer in ['F.Fab', 'F.CrtYd']:
            generate_switch_layer(kicad_mod, layer, size, data)

        for layer in ['Dwgs.User']:
            generate_keysize_layer(kicad_mod, layer, size, data)

        for layer in ['F.SilkS']:
            generate_switch_layer(kicad_mod, layer, size, data)
        
        for layer in ['H.Pads']:
            generate_pads_layer(kicad_mod, layer, size, data)
            
        for layer in ['H.Stabs']:
            generate_stabs_layer(kicad_mod, layer, size, data)

        # add model
        kicad_mod.append(Model(filename="${KISYS3DMOD}/Button_Switch_Keyboard.3dshapes/" + footprint_name + '.wrl'
                              ,at=[0,0,0]
                              ,scale=[1,1,1]
                              ,rotate=[0,0,0]))

        # write file
        file_handler = KicadFileHandler(kicad_mod)
        file_handler.writeFile(footprint_name + '.kicad_mod')

if __name__ == '__main__':
    gen_key("SW_Cherry_MX_{size}_PCB"
           ,"Cherry MX keyswitch, {size}, PCB mount, http://cherryamericas.com/wp-content/uploads/2014/12/mx_cat.pdf"
           ,"Cherry MX keyswitch {size} PCB"
           , cherry_switch_pcb)
    gen_key("SW_Cherry_MX_{size}_Plate"
           ,"Cherry MX keyswitch, {size}, Plate mount, http://cherryamericas.com/wp-content/uploads/2014/12/mx_cat.pdf"
           ,"Cherry MX keyswitch {size} Plate"
           , cherry_switch_plate)
    gen_key("SW_Matias_{size}"
           ,"Matias/ALPS keyswitch, {size}, http://matias.ca/switches/"
           ,"Matias ALPS keyswitch {size}"
           , matias_switch)

    gen_key("SW_Gateron_KS8_{size}"
           ,"Gateron KS8 keyswitch, {size}, http://www.gateron.com/supply/189.html"
           ,"Gateron KS8 MX keyswitch SMD {size}"
           , gateron_switch_smd_plate)
