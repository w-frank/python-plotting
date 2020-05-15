class custom_plotting:
    def setup_plots(self,  fontsize=8, usetex=True):
        """
        This function adjusts the default matplotlib settings so that all
        figures have the same feel.

        Note that with usetex=True, fonts are rendered with LaTeX. This may
        result in an error if LaTeX is not installed. In that case you can set usetex to False.
        """
        import matplotlib
        self.fontsize = fontsize
        self.usetex = usetex
        matplotlib.rc('legend', fontsize=self.fontsize, handlelength=3)
        matplotlib.rc('axes', titlesize=self.fontsize)
        matplotlib.rc('axes', labelsize=self.fontsize)
        matplotlib.rc('xtick', labelsize=self.fontsize)
        matplotlib.rc('ytick', labelsize=self.fontsize)
        matplotlib.rc('text', usetex=self.usetex)
        matplotlib.rc('font', size=self.fontsize, family='serif',
                        style='normal', variant='normal',
                        stretch='normal', weight='bold')
        matplotlib.rc('patch', force_edgecolor=True)
        matplotlib.rc('grid', linestyle=':')
        matplotlib.rc('errorbar', capsize=3)
        matplotlib.rc('image', cmap='viridis')
        matplotlib.rc('axes', xmargin=0)
        matplotlib.rc('axes', ymargin=0)
        matplotlib.rc('xtick', direction='in')
        matplotlib.rc('ytick', direction='in')
        matplotlib.rc('xtick', top=True)
        matplotlib.rc('ytick', right=True)
