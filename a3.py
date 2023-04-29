""" 
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

Ilan Klimberg (idk7), Aaron Baruch (amb565)
10/02/2022
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    return introcs.RGB(255 - rgb.red, 255 - rgb.green, 255 - rgb.blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
        str5(1e-9)    is  '0.000'
    
    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    value_string = str(value)
    dec_index = value_string.find('.')
    if dec_index == 1:
        value = str(round(value, 3))[:5]
        if len(str(value)) < 5:
            value = str(value) + '000'
            value = value[:5]
    elif dec_index == 2:
        value = str(round(value, 2))[:5]
        if len(str(value)) < 5:
            value = str(value) + '0'
    elif dec_index == 3:
        value = str(round(value, 1))[:5]
        if len(str(value)) < 5:
            value = str(value) + '00'
    if 'e-' in str(value) or 'E-' in str(value):
        value = round(value)
        value = str(value) + '.000'
    if str(value).find('.') == -1 and 'e' not in str(value):
        value = str(value) + '.0000'
        value = value[:5]
    return value


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    #example (98.448, 25.362, 72.8, 1.0))
    c = str5(cmyk.cyan)
    m = str5(cmyk.magenta)
    y = str5(cmyk.yellow)
    k = str5(cmyk.black)
    string_cmyk = '(' + c + ', ' + m + ', ' + y + ', ' + k + ')'
    return string_cmyk


def str5_hsv(hsv):
    """
    Returns the string representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    h = hsv.hue
    s = hsv.saturation
    v = hsv.value
    return '(' + str5(h) + ', ' + str5(s) + ', ' + str5(v) + ')'


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.
    
    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.
    red = rgb.red/255.0
    green = rgb.green/255.0
    blue = rgb.blue/255.0
    k = 1 - max(red,green,blue)
    if(k == 1):
        return introcs.CMYK(0,0,0,k*100)
    else:
        c = (1-red-k)/(1-k) * 100
        m = (1-green-k)/(1-k) * 100
        y = (1-blue-k)/(1-k) * 100
        k = k * 100
        return introcs.CMYK(c,m,y,k)


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk
    
    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0. 
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()
    c = cmyk.cyan/100.0
    m = cmyk.magenta/100.0
    y = cmyk.yellow/100.0
    k = cmyk.black/100.0
    r = ((1-c)*(1-k)) * 255.0
    g = ((1-m)*(1-k)) * 255.0
    b = ((1-y)*(1-k)) * 255.0
    return introcs.RGB(round(r),round(g),round(b))


def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
   
    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    r = rgb.red/255.0
    g = rgb.green/255.0
    b = rgb.blue/255.0
    maximum = max(r , g, b)
    minimum = min(r, g, b)
    if(maximum == minimum):
        h = 0
    elif(maximum == r and g >= b):
        h = 60.0 * (g-b) / (maximum - minimum)
    elif(maximum == r and g < b):
        h = 60.0 * (g-b) / (maximum - minimum) + 360.0
    elif(maximum == g):
        h = 60.0 * (b-r) / (maximum - minimum) + 120.0
    elif (maximum == b):
        h = 60.0 * (r-g) / (maximum - minimum) + 240.0
    s = 0
    if (maximum != 0):
        s = 1 - (minimum/maximum)
    v = maximum
    return introcs.HSV(h,s,v)
    

def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    h_i = math.floor(hsv.hue/60)
    f = hsv.hue/60 - h_i
    p = hsv.value * (1-hsv.saturation)
    q = hsv.value * (1 - f*hsv.saturation)
    t = hsv.value * (1 - (1 - f) * hsv.saturation)

    r = 0
    if (h_i == 0):
        r = hsv.value
        g = t 
        b = p
    elif (h_i == 1):
        r = q 
        g = hsv.value 
        b = p 
    elif (h_i == 2):
        r = p 
        g = hsv.value
        b = t
    elif (h_i == 3):
        r = p 
        g = q 
        b = hsv.value
    elif (h_i == 4):
        r = t
        g = p 
        b = hsv.value
    elif (h_i == 5):
        r = hsv.value
        g = p 
        b = q
    return introcs.RGB(round(r*255.0), round(g*255.0), round(b*255.0))


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast
    
    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart, 
    with all values becoming 0 or 1 when contrast = 1.
    
    Parameter value: the value to adjust
    Precondition: value is a float in 0..1
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    if (contrast >= -1 and contrast < 1):
        if (value < 0.25 + (0.25 * contrast)):
            y = ((1 - contrast)/(1 + contrast)) * value
        elif (value > 0.75 - (0.25 * contrast)):
            y = (((1 - contrast)/(1 + contrast)) * \
                (value - ((3 - contrast)/4)) + ((3 + contrast)/4))
        else:
            y = (((1 + contrast)/(1 - contrast)) * \
                (value - ((1 + contrast)/4)) + ((1 - contrast)/4))
    else:
        if (value >= 0.5):
            y = 1
        else:
            y = 0
    return y


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb
    
    This function is a PROCEDURE.  It modifies rgb and has no return value.  It should
    apply contrast_value to the red, blue, and green values.
    
    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    r = rgb.red/255.0
    g = rgb.green/255.0
    b = rgb.blue/255.0

    rgb.red = round(255.0 * contrast_value(r, contrast))
    rgb.green = round(255.0 * contrast_value(g, contrast))
    rgb.blue = round(255.0 * contrast_value(b, contrast))