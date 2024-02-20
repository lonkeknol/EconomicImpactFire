from matplotlib import pyplot as plt
import numpy as np


def graph_cost_distribution(total_cost_no_spr, total_cost_spr):
    ### Visualization of cost distribution per design
    fig, ax = plt.subplots()
    labels=['no sprinkler','sprinkler']
    categories=['direct loss building','direct loss contents','indirect loss','fatalities','injuries','investment','maintenance','obsolescene']
    bar_width = 0.35

    cumCost=np.array([0,0])
    for i, cat in enumerate(categories):
        ax.bar(labels,[total_cost_no_spr[i], total_cost_spr[i]], bar_width, bottom=cumCost, label=cat)
        cumCost=cumCost+np.array([total_cost_no_spr[i], total_cost_spr[i]])

    ax.set_ylim((0,12000))
    ax.set_ylabel('PNV costs [USD]')
    ax.set_title('Total PNV cost of design alternative')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1])
    fig.set_size_inches(10,8)

    return fig


def graph_indirect_cost(m_vsl, indirect_cost, m_z, m_eta_sprinkler):
    fig,ax = plt.subplots(1,1)

    color = (['r','r','r','b','b','b','g','g','g'])
    linestyle = (['solid','dashed','dashdot','solid','dashed','dashdot','solid','dashed','dashdot'])

    legends = []
    for num in np.arange(len(m_vsl)):
        ax.plot(indirect_cost, m_z[:,num]/1e3, linestyle=linestyle[num], color=color[num])
        legends.append(f"VSL = {m_vsl[num]/1e6}, $\eta_{{sprinkler}}$ = {m_eta_sprinkler[num]}")

    ax.plot([0,300],[0,0],linestyle='solid',color='k',linewidth=3.0)
    ax.text(10,0.15,'Z = 0')
    ax.set_xlim([0,300])
    ax.set_yticks([-2,0,2,4,6,8,10,12,14,16])
    ax.set_xlabel('Indirect cost as percentage of direct costs [%]') 
    ax.set_ylabel('Present net value, $Z$ [$10^3 $ USD]')
    ax.legend(legends,fontsize=12)

    fig.set_size_inches(12,8)

    return fig
