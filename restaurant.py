from pywebio.input import input as input_pw, NUMBER, slider, checkbox, select
from pywebio.output import put_markdown, put_success, put_error, put_image, put_warning, put_text, put_row, put_column
import messages_rest
import images
import prices

guest_name = input_pw(messages_rest.MSG_WELCOME_GUEST, required=True)
put_success(messages_rest.MSG_WELCOME_GUEST_WITH_NAME.format(name=guest_name))
# put_error(messages_rest.MSG_WELCOME_GUEST_WITH_NAME.format(name=guest_name))
# put_warning(messages_rest.MSG_WELCOME_GUEST_WITH_NAME.format(name=guest_name))

put_markdown("## Меню")

put_row(
    [
        put_column(
            [put_image(images.PIZZA_IMAGE, width='180px', height='120px'), put_text(f'Піцца {prices.PIZZA_PRICE}')]),
        put_column(
            [put_image(images.BURGER_IMAGE, width='180px', height='120px'), put_text(f'Бургер {prices.BURGER_PRICE}')]),
        put_column(
            [put_image(images.COLA_IMAGE, width='180px', height='120px'), put_text(f'Кола {prices.COLA_PRICE}')]),
        put_column(
            [put_image(images.CAUSE_IMAGE, width='180px', height='120px'), put_text(f'Соуси {prices.CAUSE_PRICE}')]),
    ]
)
# put_row(
#     [
#         put_column(
#             [put_image(images.COLA_IMAGE, width='180px', height='120px'), put_text(f'Кола {prices.COLA_PRICE}')]),
#         put_column(
#             [put_image(images.CAUSE_IMAGE, width='180px', height='120px'), put_text(f'Соуси {prices.CAUSE_PRICE}')]),
#     ]
# )

# get quantity
pizza_quantity = input_pw(label='Pizza', type=NUMBER, value=1)
burger_quantity = slider(label='Burger', min_value=0, max_value=10, value=2)
causes = checkbox(label='Causes', options=['майонез', 'кетчуп', 'гірчиця'])
causes_quantity = len(causes)

cola = select("Cola", options=['-', 'класична', 'light'])
cola_quantity = 0
if cola != '-':
    cola_quantity = 1

# calculate total prices
total_cost_pizza = pizza_quantity * prices.PIZZA_PRICE
total_cost_burger = burger_quantity * prices.BURGER_PRICE
total_cost_cola = cola_quantity * prices.COLA_PRICE
total_cost_causes = causes_quantity * prices.CAUSE_PRICE

total_cost = total_cost_cola + total_cost_burger + total_cost_pizza + total_cost_causes

discount = 0
if total_cost > prices.DISCOUNT_LEVEL:
    discount = int(total_cost * prices.DISCOUNT_PERCENT / 100)
print(discount)
order_summ = total_cost - discount

put_markdown('## Order')
put_text('Total', total_cost)
put_text('Discount', discount)
put_text('PAY', order_summ)
put_text(causes)



#  output examples
put_warning('warning')
put_error('error')
put_success('put_success')
put_text('put_text')
put_markdown('# 1 level')
put_markdown('## 2 level')
put_markdown('### 3 level')
put_markdown('#### 4 level')
put_markdown("""
gjyhgj
**fghgfhfgh**
ghhhh     

_jhgjghjhgj_

> hfghgfhgfhfghfghf


[commit](https://github.com/smartguy-coder/group24032026/pull/9)

- [x] gfhfg
- [ ] gfhfg

2. hgfhg
""")