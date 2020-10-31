import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd



#Title on main page

st.title("Prediction of Fabric Tensile Strength")

#To create sliders on sidebar
wp_material = st.selectbox('Warp Material', ('Cotton', 'P/C'))
wt_material = st.selectbox('Weft Material', ('Cotton', 'P/C'))
a = st.slider('Warp Yarn Strength (cN)', 270, 540, 400)  # 👈 this is a widget
b = st.slider('Weft Yarn Strength (cN)', 270, 540, 400)
c = st.slider('Ends per cm', 40, 80, 60)
d = st.slider('Picks per cm', 40, 80, 60)
e = st.slider('Fabric Float Length', 1, 3, 2)

#a = wpYs; b = wtYs; c = E; d = P; e=FL
# m1wp[warp fabric strength] and m1wt[weft fabric strength], m1wt equation is for pc warp, pc weft
m1wp = int((-5) -(0.37 * a)+(0.09 * b)-(0.72 * c)+(1.22 * d)-(14.89 * e)+(0.02 * c * a))
m1wt = int((-41) +(0.07 * a)-(0.23 * b)+(0.85 * c)+(0.15 * d)-(14.01 * e)+(0.02* d * b))

#FTSwp = - 5 - 0.37YSwp + 0.09YSwt - 0.72E + 1.22P - 14.89FL + 0.02E *YSwp
#FTSwt = - 41 + 0.07YSwp - 0.23YSwt + 0.85E + 0.15P - 14.01FL + 0.02P *YSwt

#warp PC, weft cotton
m2wp = int((- 14.63) -(0.37 * a)+(0.14 * b)-(0.76 * c)+(0.89 * d)-(16.5 * e)+(0.023 * c * a))
m2wt = int((- 167.43) +(0.05 * a)+(0.08 * b)+(0.96 * c)+(1.8 * d)-(10.35 * e)+(0.014* d * b))

#FTSwp= - 14.63 - 0.37YSwp + 0.14 YSwt - 0.76E + 0.89P – 16.5FL + 0.023E*YSwp
#FTSwt = - 167.43 + 0.05YSwp + 0.08YSwt + 0.96E + 1.8P - 10.35FL + 0.014P *YSwt 
#warp cotton, weft cotton
m3wp = int((55.01) -(0.5 * a)+(0.06 * b)-(1.85 * c)+(0.88 * d)-(13.8 * e)+(0.025 * c * a))
m3wt = int((37.1) +(0.03 * a)-(0.38 * b)+(0.72 * c)-(1.64 * d)-(13.5 * e)+(0.023* d * b))

#FTSwp = 55.01 - 0.5YSwp+ 0.06YSwt – 1.85E + 0.88P – 13.8FL + 0.025E*YSwp 
#FTSwt = 37.1+ 0.03YSwp - 0.38YSwt + 0.72E - 1.64P - 13.5FL + 0.023P*YSwt 

#warp cotton, weft pc
m4wp = int((58.77) -(0.38 * a)+(0.04 * b)+(0.97 * c)+(0.59 * d)-(12.8 * e)+(0.015 * c * a))
m4wt = int((- 33.07) +(0.05 * a)-(0.16 * b)+(0.42 * c)+(1.04 * d)-(12.4 * e)+(0.018* d * b))

#FTSwp = 58.77 - 0.38YSwp + 0.04YSwt + 0.97E + 0.59P - 12.8FL + 0.015E*YSwp 
#FTSwt = - 33.07 + 0.05YSwp - 0.16YSwt + 0.42E + 1.04P - 12.4FL + 0.018P*YSwt 


#To show results on the main page, under the heading 
left_column, right_column = st.beta_columns(2)
left_column.subheader("Fabric Tensile Strength (Warp), N")
right_column.subheader("Fabric Tensile Strength (Weft), N")

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
    
#Part 2: for prediction of yarn strength
st.title("Prediction of Yarn Strength")
st.write("for producing fabric of specific strength")
wpy_material = st.selectbox('Warp Yarn Material', ('Cotton', 'P/C'))
wty_material = st.selectbox('Weft Yarn Material', ('Cotton', 'P/C'))


#To create sliders on sidebar

X = st.slider('Warp Yarn linear density (tex)', 15, 30, 20)  # 👈 this is a widget
Y = st.slider('Weft Yarn linear density (tex)', 15, 30, 20)

FTSwp = st.slider('Fabric Warp Strength (N)', 130, 850, 400)
FTSwt = st.slider('Fabric Weft Strength (N)', 130, 850, 400)

E = st.slider('Ends/ cm', 40, 80, 60)
P = st.slider('Picks/ cm', 40, 80, 60)
FL = st.slider('Float Length', 1, 3, 2)

YSwp1 = int ((FTSwp)+(15.07)-(2.29 * Y)+(0.72 * E)-(1.22 * P)+(14.9 * FL))/((0.02 * E)-(0.37)) 
YSwt1 = int ((FTSwt)+(48.85)-(1.84 * X)-(0.85 * E)-(0.14 * P)+(14.01 * FL))/((0.02 * P)-(0.23)) 

YSwp2 = int ((FTSwp)+(24.75)-(2.65 * Y)+(0.76 * E)-(0.89 * P)+(16.5 * FL))/((0.023 * E)-(0.37))
YSwt2 = int ((FTSwt)+(173.16)-(1.41 * X)-(0.96 * E)-(1.79 * P)+(10.35 * FL))/((0.014 * P)+(0.08))

YSwp3 = int ((FTSwp)-(50.37)-(1.21 * Y)+(1.85 * E)-(0.88 * P)+(13.8 * FL))/((0.025 * E)-(0.5)) 
YSwt3 = int ((FTSwt)-(36.95)-(0.54 * X)-(0.72 * E)+(1.65 * P)+(13.51 * FL))/((0.023 * P)-(0.38)) 

YSwp4 = int ((FTSwp)-(53.56)-(1.12 * Y)-(0.97 * E)-(0.59 * P)+(12.8 * FL))/((0.015 * E)-(0.38)) 
YSwt4 = int ((FTSwt)+(38.36)-(0.94 * X)-(0.42 * E)-(1.04 * P)+(12.4 * FL))/((0.018 * P)-(0.16)) 

#To show results on the main page, under the heading 
left_column, right_column = st.beta_columns(2)
left_column.subheader("Warp Yarn Tensile Strength, cN")
right_column.subheader("Weft Yarn Tensile Strength, cN")

if wpy_material =='P/C' and wty_material =='P/C': 
    left_column.write(YSwp1)
    right_column.write(YSwt1)
elif  wpy_material =='P/C' and wty_material =='Cotton':
    left_column.write(YSwp2)
    right_column.write(YSwt2)
elif  wpy_material =='Cotton' and wty_material =='Cotton':
    left_column.write(YSwp3)
    right_column.write(YSwt3)
elif  wpy_material =='Cotton' and wty_material =='P/C':
    left_column.write(YSwp4)
    right_column.write(YSwt4)
    
st.info("Courtesy: Dr. Zulfikar Ali, National Textile University")








