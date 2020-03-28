import pygal # First import pygal
# from pygal.maps.fr import aggregate_regions


def plot_location(gd):
  occ_chart = pygal.maps.fr.Departments(human_readable=True)
  occ_chart.title = 'Polution by cities'

  fr_chart.add('Polution', gd.to_dict())

  fr_chart.render_in_browser()
  # fr_chart.render_to_file('./chart.svg')  # Write the chart in the specified file
