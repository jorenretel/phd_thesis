'''
To make the final figure in jpg format, just save the sub-plots by
hand and:

convert -append plot*.png result.png

convert result.png -colorspace RGB -resize 200% -colorspace sRGB labelling_schemes_on_ompg_sequence.png

to merge them all together.

'''


from bokeh.plotting import figure, gridplot, output_file, ColumnDataSource, show
from bokeh.models import LinearAxis, Range1d

schemes = ['TEMPQANDSG',
           'GENDQPASR',
           'MKINDT',
           'RIGA',
           'GANDSH',
           'GAFY',
           'GAVLS',
           'GAFYSHVL',
           'SHLYGWAFV']

sequence = list('MEERNDWHFNIGAMYEIENVEGYGEDMDGLAEPSVYFNAANGPWRIALAYYQEGPVDYSAGKRGTWFDRPELEVHYQFLENDDFSFGLTGGFRNYGYHYVDEPGKDTANMQRWKIAPDWDVKLTDDLRFNGWLSMYKFANDLNTTGYADTRVETETGLQYTFNETVALRVNYYLERGFNMDDSRNNGEFSTQEIRAYLPLTLGNHSVTPYTRIGLDRWSNWDWQDDIEREGHDFNRVGLFYGYDFQNGLSVSLEYAFEWQDHDEGDSDKFHYAGVGVNYSF')

# Really dirty hack to make every category 'unique'. Bokeh needs this for
# plotting the x-axis labels correctly.
xlabels = [" "*i +r + " "*i for i,r in enumerate(sequence)]

color = []
rate = []
residue = []
scheme = []
colabels = []

current_color = '#1b9e77'


def new_color():

    colors = ['#1b9e77', '#d95f02', '#7570b3']
    i = colors.index(current_color)
    return colors[(i+1) % 3]


cluster = [sequence[0]]
clusters = [cluster]

for resA, resB in zip(sequence[:-1], sequence[1:]):

    for s in schemes:
        if resA in s and resB in s:
            cluster.append(resB)
            break
    else:
        cluster = [resB]
        clusters.append(cluster)

average_cluster_length = sum([len(cluster) for cluster in clusters])/float(len(clusters))
print 'average cluster length is {}.'.format(average_cluster_length)

weighted_average = '''The weighted average, when a residue is picked
                      randomly, it is part of a cluster that is on
                      average of length {}.

                   '''.format(sum([len(cluster)**2 for cluster in clusters])/281.0)
print weighted_average


i = 0
for cluster in clusters:

    if len(cluster) == 1:
        c = 'grey'
    else:
        c = current_color = new_color()

    for r in cluster:
        i += 1
        colabel = False
        for s in schemes:
            residue.append(i)
            scheme.append(s)
            if r in s:
                color.append(c)
                rate.append(1)
            else:
                color.append("white")
                rate.append(0)


output_file('labelling_scheme_plot.html')
TOOLS = "resize,save"
sub_plots = []

for start, stop in [(0,60),(60,120),(120,180),(180,240), (240,281)]:

    xl = xlabels[start:stop]
    start_point = start * len(schemes)
    stop_point = stop * len(schemes)
    plot_width = (stop - start) *16

    source = ColumnDataSource(data=dict(scheme=scheme[start_point:stop_point],
                                        residue=[r - residue[start_point]+1 for r in residue[start_point:stop_point]],
                                        color=color[start_point:stop_point],
                                        rate=rate[start_point:stop_point]))

    p = figure(title=None,
               x_range=xl, y_range=schemes,
               x_axis_location="above", plot_width=plot_width,
               plot_height=200, toolbar_location="left", tools=TOOLS)

    p.rect("residue", "scheme", 1, 1, source=source,
           color="color", line_color=None)

    p.min_border_bottom = 10

    p.extra_x_ranges = {"foo": Range1d(start=start+0.5, end=stop+0.5)}
    p.add_layout(LinearAxis(x_range_name="foo", minor_tick_line_color=None), 'below')

    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font = "Tex Gyre Pagella"
    p.axis.major_label_text_font_size = "10pt"
    p.axis.major_label_text_color = 'black'
    p.axis.major_label_standoff = 0

    sub_plots.append([p])


total_plot = gridplot(sub_plots)
total_plot.min_border_bottom = 0

show(total_plot)
