def enrichr_plot(dataframe,title,left):
    import plotly
    import plotly.plotly as py
    import plotly.graph_objs as go
    plotly.tools.set_credentials_file(username='gnovikov', api_key='sZtLSfuA05u066Fy05zD')
    dataframe_list=dataframe[1][:10].tolist()
    dataframe_list.reverse()
    dataframe_score=dataframe[4][:10].values.tolist()
    dataframe_score.reverse()

    dataframe_plot=[go.Bar(
                x=dataframe_score,
                y=dataframe_list,
                orientation = 'h',
    marker=dict(
            color='ef2e4e',
            line=dict(
                color='rgb(8,48,107)',
                width=1,
            )
        ),
        opacity=0.8
    )]
                          
    layout = go.Layout(title=title,
                       titlefont=dict(
                family='Times New Roman',
                           
                size=20
            ),
                       margin=go.Margin(l=left,r=15,b=50,t=150,
                                    ))
        

    fig = go.Figure(data=dataframe_plot, layout=layout)
    return py.iplot(fig, filename=title,layout=layout)



def plot_3d_scatter(x,y,z,size,text='', title='', color_by=None, xlab='x', ylab='y', zlab='z', colors=["#3366cc", "#dc3912", "#ff9900", "#109618", "#990099", "#0099c6", "#dd4477", "#66aa00", "#b82e2e", "#316395", "#994499", "#22aa99", "#aaaa11", "#6633cc", "#e67300", "#8b0707", "#651067", "#329262", "#5574a6", "#3b3eac"]):
        import plotly.graph_objs as go
        from plotly.offline import iplot
        import plotly.offline as py
        import numpy as np
        
	# Plot it
	if str(color_by) == 'None':
		trace = go.Scatter3d(
			x=x,
			y=y,
			z=z,
			mode='markers',
			text=text,
			marker=dict(
				size=12,
				opacity=0.8
			)
		)
		data = [trace]
	else:
		data = []
		for index, term in enumerate(set(color_by)):
			indices = [i for i,e in enumerate(color_by) if e == term]
			data.append(go.Scatter3d(
				x=[x[i] for i in indices],
				y=[y[i] for i in indices],
				z=[z[i] for i in indices],
				mode='markers',
				text=[text[i] if type(text) == list else '' for i in indices],
				name=term,
				marker=dict(
					size=size,
					opacity=0.8,
					color=colors[index]
				)
			))


	go.layout = go.Layout(
		title=title,
                showlegend=True,
		margin=dict(
			l=0,
			r=0,
			b=0,
			t=50
		),
		scene = dict(
			xaxis = dict(
				title = xlab
			),
			yaxis = dict(
				title = ylab
			),
			zaxis = dict(
				title = zlab
			)
		)
	)
	fig = go.Figure(data=data, layout=go.layout)
	return py.iplot(fig)

def plot_2d_scatter(x,y,size,text='',title='', xlab='x', ylab='y',color_by=None,colors=["#3366cc", "#dc3912", "#ff9900", "#109618", "#990099", "#0099c6", "#dd4477", "#66aa00", "#b82e2e", "#316395", "#994499", "#22aa99", "#aaaa11", "#6633cc", "#e67300", "#8b0707", "#651067", "#329262", "#5574a6", "#3b3eac"]):
        import plotly.graph_objs as go
        from plotly.offline import iplot
        import numpy as np
	if str(color_by) == 'None':
		trace = go.Scatter(
			x=x,
			y=y,
			mode='markers',
			text=text,
                        
			marker=dict(
				size=12,
				opacity=0.8,
				color='black'
			)
		)
		data = [trace]
	else:
		data = []
		for index, term in enumerate(set(color_by)):
			indices = [i for i,e in enumerate(color_by) if e == term]
			data.append(go.Scatter(
				x=[x[i] for i in indices],
				y=[y[i] for i in indices],
				mode='markers',
				text=[text[i] if type(text) == list else '' for i in indices],
				marker=dict(
					size=size,
					opacity=0.8,
					color=colors[index]
				)
			))

	go.layout = go.Layout(
		title=title,
		hovermode='closest',
                showlegend=False,
		xaxis = dict(
                    
			title = xlab
		),
		yaxis = dict(
			title = ylab
		)
	)
	fig = go.Figure(data=data, layout=go.layout)
	return iplot(fig)




    

def double_volcano (x_sign1,y_sign1,x_insign1,y_insign1,x_sign2,y_sign2,x_insign2,y_insign2,name_sign,name_insign,title1,title2,xaxis,yaxis,major_title,size):
    
    import plotly
    plotly.tools.set_credentials_file(username='gnovikov', api_key='sZtLSfuA05u066Fy05zD')
    import plotly.plotly as py
    import plotly.graph_objs as go
    from plotly.offline import iplot
    import numpy as np
    from plotly import tools
   

    trace_sign_1 = go.Scatter(
        x = x_sign1,
        y = y_sign1,
        xaxis=xaxis,
        yaxis=yaxis,
        name = name_sign,
        mode = 'markers',
        marker=dict(size=size, opacity=0.8,color='#dc3912'
)
        )


    trace_insign_1 = go.Scatter(
        x = x_insign1,
        y = y_insign1,
        xaxis=xaxis,
        yaxis=yaxis,
        name = name_insign,
        mode = 'markers',
         marker=dict(size=size, opacity=0.8,color='#3366cc'
)
        )
    
    
    trace_sign_2 = go.Scatter(
        x = x_sign2,
        y = y_sign2,
        showlegend=False,
        mode = 'markers',
        marker=dict(size=size, opacity=0.8,color='#dc3912'
)
        )


    trace_insign_2 = go.Scatter(
        x = x_insign2,
        y = y_insign2,
        showlegend=False,
        mode = 'markers',
         marker=dict(size=size, opacity=0.8,color='#3366cc'
)
        )
    

    fig = tools.make_subplots(rows=1, cols=2,subplot_titles=(title1,title2),)
    
    fig['layout']['xaxis1'].update(title=xaxis)
    fig['layout']['xaxis2'].update(title=xaxis)


    fig['layout']['yaxis1'].update(title=yaxis)
    fig['layout']['yaxis2'].update(title=yaxis)

    fig['layout'].update(title=major_title)

    fig.append_trace(trace_sign_1, 1, 1)
    fig.append_trace(trace_insign_1, 1, 1)
    fig.append_trace(trace_sign_2, 1, 2)
    fig.append_trace(trace_insign_2, 1, 2)
    

    py.iplot(fig, filename='volcano_scatter')
    return iplot(fig)


def venn(in_label1,in_label2,inter_label,name1,name2,color1,color2,color_inter):
    from matplotlib import pyplot as plt
    from matplotlib_venn import venn2, venn2_circles


    # Subset sizes
    s = (
        50,  # Ab
        50,  # aB
        50,  # AB
    )

    v = venn2(subsets=s, set_labels=(name1, name2))

    # Subset labels
    v.get_label_by_id('10').set_text(in_label1)
    v.get_label_by_id('01').set_text(in_label2)
    v.get_label_by_id('11').set_text(inter_label)

    # Subset colors
    v.get_patch_by_id('10').set_color(color1)
    v.get_patch_by_id('01').set_color(color2)
    v.get_patch_by_id('11').set_color(color_inter)

    # Subset alphas
    v.get_patch_by_id('10').set_alpha(0.2)
    v.get_patch_by_id('01').set_alpha(0.2)
    v.get_patch_by_id('11').set_alpha(0.5)

    # Border styles
    c = venn2_circles(subsets=s, linestyle='solid')
    c[0].set_ls('solid')  # Line style
    c[0].set_lw(2.0)       # Line width

    return plt.show()





def volcano (x_sign1,y_sign1,x_insign1,y_insign1,name_sign,name_insign,xaxis,yaxis,major_title,size):
    
    import plotly
    plotly.tools.set_credentials_file(username='gnovikov', api_key='sZtLSfuA05u066Fy05zD')
    import plotly.plotly as py
    import plotly.graph_objs as go
    from plotly.offline import iplot
    import numpy as np
    from plotly import tools
   

    trace_sign_1 = go.Scatter(
        x = x_sign1,
        y = y_sign1,
        xaxis=xaxis,
        yaxis=yaxis,
        name = name_sign,
        mode = 'markers',
        marker=dict(size=size, opacity=0.8,color='#dc3912'
)
        )


    trace_insign_1 = go.Scatter(
        x = x_insign1,
        y = y_insign1,
        xaxis=xaxis,
        yaxis=yaxis,
        name = name_insign,
        mode = 'markers',
         marker=dict(size=size, opacity=0.8,color='#3366cc'
)
        )
    
    fig = tools.make_subplots(rows=1, cols=1)
    
    fig['layout']['xaxis1'].update(title=xaxis)
 
    fig['layout']['yaxis1'].update(title=yaxis)
 

    fig['layout'].update(title=major_title)

    fig.append_trace(trace_sign_1, 1, 1)
    fig.append_trace(trace_insign_1, 1, 1)

    

    py.iplot(fig, filename='volcano_scatter')
    return iplot(fig)











    


