from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404

from tethys_sdk.gizmos import TableView,TextInput, SelectInput, Button, LinePlot


@login_required()
def home(request):
	"""
	Controller for the home page.
	"""
	#Define View Options
	context={}

	return render(request, 'fdc/home.html',context)

def results(request):
	"""
	Controller for the results page.
	"""
	if request.POST and 'submit' in request.POST:
		session=SessionMaker()

		flowlist=results
		plotData=[]
		for i in flowlist:
			value=list(i)
			plotData.append(value)

		fdc_tbv=TableView(column_names=('Percent (%)', unicode('Flow (M'+u'\u00b2'+' /S)')),
			rows=flowlist,
			hover=True,
			striped=True,
			bordered=True,
			condensed=True,
			editable_columns=(False,False,False),
			row_ids=[range(0,len(flowlist))])
		plot_view=LinePlot(height='100%',
			width='100%', 
			engine='highcharts',
			title='Flow-Duration Curve', 
			spline=True,
			x_axis_title='Percent (%)',
			y_axis_title='Flow',
			y_axis_units='m^3/s',
			series=[{'name':'Flow',
			'color': '#277554',
			'marker':{'enabled':False},
			'data': plotData}]
			)
		session.close()


		context = {'fdc_tbv':fdc_tbv,
		'plot_view': plot_view}
	#else: 
		#raise Http404("No request submitted.")


	return render(request, 'fdc/results.html',context)


