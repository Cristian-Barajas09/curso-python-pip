import matplotlib.pyplot as plt

def generate_bar_chart(name,labels,values):
    fig,ax = plt.subplots()
    ax.bar(labels, values)
    print(name)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def genereta_pie_chart(labels,values):
    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.savefig('./imgs/chart_pie.png')
    plt.close()
if __name__ == "__main__":
    labels = ['a','b','c']
    values = [10,40,800]
    # generate_bar_chart(labels,values)
    genereta_pie_chart(labels,values)