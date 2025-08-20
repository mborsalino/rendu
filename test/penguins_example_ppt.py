import seaborn as sns
import matplotlib as mpl
from datetime import date
from rendu.pptdeck import PptSlideDeck 

# ----------------------------------------------- #
# Use pandas/seaborn to perform some data analysis
# ----------------------------------------------- #
mpl.use('AGG')
penguins = sns.load_dataset('penguins')
fig = sns.displot(penguins, x='flipper_length_mm')
fig.savefig('./penguins_histogram.png')
flen_ave = penguins.flipper_length_mm.mean().round(2)
flen_med = penguins.flipper_length_mm.median().round(2)
flen_std = penguins.flipper_length_mm.std().round(2)
penguins.to_csv('./penguins.csv')

# ------------------------------------------------------ #
# Now use rendu to quickly assemple a PPT presentation
# ------------------------------------------------------ #

rep = PptSlideDeck()
rep.add_title_slide(f'Analysis Of Penguin Population [{date.today()}]')
rep.add_figure_slide('Flipper Length Distribution',
                     './penguins_histogram.png',
                     fit_to_width=True)

rep.save('penguin_report.pptx')



