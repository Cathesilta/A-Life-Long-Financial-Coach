# This script compare different 


import matplotlib.pyplot as plt
import yaml


# def f1(func):
#     def wrapper():
#         print('started')
#         func()
#         print('ended')
        
#     return wrapper


# def f2():
#     print('helloworld')

# f1(f2)()
# print(f1(f2)())

# Income = {}
# Income['Fixed_Salary'] = {}
# I

# r = 1/20
# print(26000*(1+r)**4)
# print(1500//12)

# print((100*8+200*4)//12)

                    
# print('total food a week full-time job:', (15*5+70*5+15*4+200)*4)
# print('total food a week full-time job meal prep:', (20*5+30*5+15*4+200)*4)
# print('total food a week freelancer:', (30*7+200)*4)


if __name__ == "__main__":
    print(24%12)
    with open('./config/income.yml', 'r') as f:
        income = yaml.safe_load(f)
    with open('./config/cost.yml') as f:
        cost = yaml.safe_load(f)
        
    
    monthly_cost = 0
    for main_type_cost in cost:
        for _, cost_value in cost[main_type_cost].items():
            monthly_cost += cost_value
    print('Your Monthly Cost is ', monthly_cost)
    monthly_cost2 = monthly_cost-4500
    
    
    for plans in income:
        if plans == 'Plan1':
            monthly_income_p1 = list(range(0,12*7))
            plan1_income_net = 0
            for month in range(0, 12*7):
                for type_of_income,income_attr in income['Plan1']['Monthly'].items():

                    if month < income_attr['estimate_profit_month']:
                        continue
                    else:
                        plan1_income_net += income_attr['monthly_net']
                plan1_income_net -= monthly_cost
                monthly_income_p1[month] = plan1_income_net
                if month%12 ==0:
                    print(f'in the {month//12} year, my plan 1 net income will be {plan1_income_net}')
            print('-----------')
        elif plans == 'Plan2':        
            monthly_income_p2 = list(range(0,12*7))
            plan2_income_net = 0
            for month in range(0, 12*7):
                for type_of_income,income_attr in income['Plan2']['Monthly'].items():
                
                    if month < income_attr['estimate_profit_month']:
                        continue
                    else:
                        plan2_income_net += income_attr['monthly_net']
                plan2_income_net -= monthly_cost2
                monthly_income_p2[month] = plan2_income_net
                    
                if month%12 ==0:
                    print(f'in the {month//12} year, my plan 2 net income will be {plan2_income_net}')
                    
                    
    months = list(range(1, len(monthly_income_p1) + 1))
    plt.plot(months, monthly_income_p1, label='Plan 1')
    plt.plot(months, monthly_income_p2, label='Plan 1')
    # Adding circle markers at every 12th point
    for i in range(len(monthly_income_p1)):
        if (i + 1) % 12 == 0:  # +1 to account for zero indexing if you want the 12th, 24th, etc., points
            plt.plot(months[i], monthly_income_p1[i], 'o', color='k', label='Every 12th point' if i == 11 else "")
            plt.plot(months[i], monthly_income_p2[i], 'o', color='m', label='Every 12th point' if i == 11 else "")
    plt.xticks(range(0, len(months)+1, 12))
    plt.gca().ticklabel_format(style='plain', axis='y', useOffset=False)

    # Adding title and labels
    plt.title('Curve with Circle Markers at Every 12th Data Point')
    plt.xlabel('Month')
    plt.ylabel('Chinese Yuan')
    plt.legend()

    # Showing the plot
    plt.show()