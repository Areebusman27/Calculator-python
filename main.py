import streamlit as st


st.title('Calculator')

num1 = st.number_input('Enter the first number')
num2 = st.number_input('Enter the second numnber')

select_operation = st.selectbox('Choose operation',['Add','Subtract','Multiply','Divide'])

if st.button('Calculate'):
    if select_operation == "Add":
        result = num1 + num2
        st.success(f'Result = {result}')
    elif select_operation == 'Subtract':
        result = num1 - num2
        st.success(f'Result = {result}')
    elif select_operation == 'Multiply':
        result = num1 * num2
        st.success(f'Result = {result}')
    elif select_operation == 'Divide':
        if num2 != 0:
            result = num1 / num2
            st.success(f'Result = {result}')
        else:
            st.success('Cannot be divided by zero')
   
    



