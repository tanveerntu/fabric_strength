import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd



#Title on main page

st.title("Prediction of Fabric Tensile Strength")

#To create sliders on sidebar
left_column, right_column = st.beta_columns(2)
wp_material = left_column.selectbox('Warp Material', ('Cotton', 'P/C'))
wt_material = right_column.selectbox('Weft Material', ('Cotton', 'P/C'))
a = left_column.slider('Warp Yarn Strength (gm)', 310, 540, 400)  # 👈 this is a widget
b = right_column.slider('Weft Yarn Strength (gm)', 310, 540, 400)
c = left_column.slider('Ends per cm', 40, 80, 60)
d = right_column.slider('Picks per cm', 40, 80, 60)
e = left_column.slider('Fabric Float Length', 1, 3, 2)

# m1wp[warp fabric strength] and m1wt[weft fabric strength], m1wt equation is for pc warp, pc weft
m1wp = int(- 5 -(0.37 * a)+(0.09 * b)-(0.72 * c)+(1.22 * d)-(14.89 * e)+(0.02 * c * a))
m1wt = int(- 41 +(0.07 * a)-(0.23 * b)+(0.85 * c)+(0.15 * d)-(14.01 * e)+(0.02* d * b))


#warp PC, weft cotton
m2wp = int(- 14.63 -(0.37 * a)+(0.14 * b)-(0.76 * c)+(0.89 * d)-(16.5 * e)+(0.023 * c * a))
m2wt = int(- 167.43 +(0.05 * a)-(0.08 * b)+(0.96 * c)+(1.8 * d)-(10.35 * e)+(0.014* d * b))

#warp cotton, weft cotton
m3wp = int(55.01 -(0.5 * a)+(0.06 * b)-(1.85 * c)+(0.88 * d)-(13.8 * e)+(0.025 * c * a))
m3wt = int(37.1 +(0.03 * a)-(0.38 * b)+(0.72 * c)+(1.64 * d)-(13.5 * e)+(0.023* d * b))

#warp cotton, weft pc
m4wp = int(58.77 -(0.38 * a)+(0.04 * b)-(0.97 * c)+(0.59 * d)-(12.8 * e)+(0.015 * c * a))
m4wt = int(- 33.07 +(0.05 * a)-(0.16 * b)+(0.42 * c)+(1.04 * d)-(12.4 * e)+(0.018* d * b))

#To show results on the main page, under the heading 

left_column.subheader("Fabric Tensile Strength (Warp)")
right_column.subheader(".")
right_column.subheader(".")
right_column.subheader("Fabric Tensile Strength (Weft)")

if wp_material =='P/C' and wt_material =='P/C': 
    left_column.write(m1wp)
    right_column.write(m1wt)
elif  wp_material =='P/C' and wt_material =='Cotton':
    left_column.write(m2wp)
    right_column.write(m2wt)
elif  wp_material =='Cotton' and wt_material =='Cotton':
    left_column.write(m3wp)
    right_column.write(m3wt)
elif  wp_material =='Cotton' and wt_material =='P/C':
    left_column.write(m4wp)
    right_column.write(m4wt)









