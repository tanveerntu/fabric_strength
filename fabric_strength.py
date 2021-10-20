import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.set_page_config(page_title="Pakistan Textile Exports",
                   page_icon=":bar_chart:"   # see different icon options at https://www.webfx.com/tools/emoji-cheat-sheet/

)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#Title on main page

st.title("Prediction of Fabric Tensile Strength")

#To create sliders on sidebar
#To show results on the main page, under the heading 
left_column, right_column = st.columns(2)

wp_material = left_column.selectbox('Select Warp Material', ('Cotton', 'P/C'))
wt_material = right_column.selectbox('Select Weft Material', ('Cotton', 'P/C'))
a = st.slider('Warp Yarn Strength (cN)', 310, 540, 400)  # 👈 this is a widget
b = st.slider('Weft Yarn Strength (cN)', 310, 540, 400)
c = st.slider('Ends per in', 40, 80, 60)
d = st.slider('Picks per in', 40, 80, 60)
e = st.slider('Fabric Float Length', 1, 3, 2)

#a = wpYs; b = wtYs; c = E; d = P; e=FL
# m1wp[warp fabric strength] and m1wt[weft fabric strength], m1wt equation is for pc warp, pc weft
m1wp = int((-5) -(0.37 * a)+(0.09 * b)-(0.72 * c)+(1.22 * d)-(14.89 * e)+(0.02 * c * a))
m1wt = int((-41) +(0.07 * a)-(0.23 * b)+(0.85 * c)+(0.15 * d)-(14.01 * e)+(0.02* d * b))


#warp PC, weft cotton
m2wp = int((- 14.63) -(0.37 * a)+(0.14 * b)-(0.76 * c)+(0.89 * d)-(16.5 * e)+(0.023 * c * a))
m2wt = int((- 167.43) +(0.05 * a)+(0.08 * b)+(0.96 * c)+(1.8 * d)-(10.35 * e)+(0.014* d * b))

#warp cotton, weft cotton
m3wp = int((55.01) -(0.5 * a)+(0.06 * b)-(1.85 * c)+(0.88 * d)-(13.8 * e)+(0.025 * c * a))
m3wt = int((37.1) +(0.03 * a)-(0.38 * b)+(0.72 * c)-(1.64 * d)-(13.5 * e)+(0.023* d * b))

#warp cotton, weft pc
m4wp = int((58.77) -(0.38 * a)+(0.04 * b)+(0.97 * c)+(0.59 * d)-(12.8 * e)+(0.015 * c * a))
m4wt = int((- 33.07) +(0.05 * a)-(0.16 * b)+(0.42 * c)+(1.04 * d)-(12.4 * e)+(0.018* d * b))

left_column1, right_column1 = st.columns(2)


if wp_material =='P/C' and wt_material =='P/C': 
    left_column1.metric(label = "Predicted Fabric Tensile Strength (Warp), N", value = m1wp)
    right_column1.metric(label = "Predicted Fabric Tensile Strength (Weft), N", value = m1wt)
elif  wp_material =='P/C' and wt_material =='Cotton':
    left_column1.metric(label = "Predicted Fabric Tensile Strength (Warp), N", value = m2wp)
    right_column1.metric(label = "Predicted Fabric Tensile Strength (Weft), N", value = m2wt)
elif  wp_material =='Cotton' and wt_material =='Cotton':
    left_column1.metric(label = "Predicted Fabric Tensile Strength (Warp), N", value = m3wp)
    right_column1.metric(label = "Predicted Fabric Tensile Strength (Weft), N", value = m3wt)
elif  wp_material =='Cotton' and wt_material =='P/C':
    left_column1.metric(label = "Predicted Fabric Tensile Strength (Warp), N", value = m4wp)
    right_column1.metric(label = "Predicted Fabric Tensile Strength (Weft), N", value = m4wt)



#Part 2: for prediction of yarn strength
st.title("Prediction of Yarn Tensile Strength")
st.write("for producing fabric of specific strength")

left_column3, right_column3 = st.columns(2)

wpy_material = left_column3.selectbox('Select Warp Yarn Material', ('Cotton', 'P/C'))
wty_material = right_column3.selectbox('Select Weft Yarn Material', ('Cotton', 'P/C'))


#To create sliders on sidebar

X = st.slider('Warp Yarn linear density (Ne)', 20, 40, 30)  # 👈 this is a widget
Y = st.slider('Weft Yarn linear density (Ne)', 20, 40, 30)
X1 = 590.5/X
Y1 = 590.5/Y

FTSwp = st.slider('Fabric Warp Strength (N)', 130, 850, 400)
FTSwt = st.slider('Fabric Weft Strength (N)', 130, 850, 400)

E = st.slider('Ends/ in', 40, 80, 60)
P = st.slider('Picks/ in', 40, 80, 60)
FL = st.slider('Float Length', 1, 3, 2)

YSwp1 = int ((FTSwp)+(15.07)-(2.29 * Y1)+(0.72 * E)-(1.22 * P)+(14.9 * FL))/((0.02 * E)-(0.37)) 
YSwt1 = int ((FTSwt)+(48.85)-(1.84 * X1)-(0.85 * E)-(0.14 * P)+(14.01 * FL))/((0.02 * P)-(0.23)) 

YSwp2 = int ((FTSwp)+(24.75)-(2.65 * Y1)+(0.76 * E)-(0.89 * P)+(16.5 * FL))/((0.023 * E)-(0.37))
YSwt2 = int ((FTSwt)+(173.16)-(1.41 * X1)-(0.96 * E)-(1.79 * P)+(10.35 * FL))/((0.014 * P)+(0.08))

YSwp3 = int ((FTSwp)-(50.37)-(1.21 * Y1)+(1.85 * E)-(0.88 * P)+(13.8 * FL))/((0.025 * E)-(0.5)) 
YSwt3 = int ((FTSwt)-(36.95)-(0.54 * X1)-(0.72 * E)+(1.65 * P)+(13.51 * FL))/((0.023 * P)-(0.38)) 

YSwp4 = int ((FTSwp)-(53.56)-(1.12 * Y1)-(0.97 * E)-(0.59 * P)+(12.8 * FL))/((0.015 * E)-(0.38)) 
YSwt4 = int ((FTSwt)+(38.36)-(0.94 * X1)-(0.42 * E)-(1.04 * P)+(12.4 * FL))/((0.018 * P)-(0.16)) 

#To show results on the main page, under the heading 

left_column2, right_column2 = st.columns(2)


if wpy_material =='P/C' and wty_material =='P/C': 
    left_column2.metric(label = "Predicted Warp Yarn Tensile Strength, cN", value = "{:,.0f}".format(YSwp1))
    right_column2.metric(label = "Predicted Weft Yarn Tensile Strength, cN", value = "{:,.0f}".format(YSwt1))
elif  wpy_material =='P/C' and wty_material =='Cotton':
    left_column2.metric(label = "Predicted Warp Yarn Tensile Strength, cN", value = "{:,.0f}".format(YSwp2))
    right_column2.metric(label = "Predicted Weft Yarn Tensile Strength, cN", value = "{:,.0f}".format(YSwt2))
elif  wpy_material =='Cotton' and wty_material =='Cotton':
    left_column2.metric(label = "Predicted Warp Yarn Tensile Strength, cN", value = "{:,.0f}".format(YSwp3))
    right_column2.metric(label = "Predicted Weft Yarn Tensile Strength, cN", value = "{:,.0f}".format(YSwt3))
elif  wpy_material =='Cotton' and wty_material =='P/C':
    left_column2.metric(label = "Predicted Warp Yarn Tensile Strength, cN", value = "{:,.0f}".format(YSwp4))
    right_column2.metric(label = "Predicted Weft Yarn Tensile Strength, cN", value = "{:,.0f}".format(YSwt4))










