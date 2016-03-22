import pymzml
import plot_v2 as pfac
handler = pymzml.run.Reader('test_Creinhardtii_QE_pH8.mzML')
fac = pfac.Factory()
count = 0


for spec in handler:
	if 11 < count < 13:
		peaks = spec.peaks
		print ('made new Plot')
		fac.newPlot(header='headerTest'+str(count))
		print('add peaks')
		fac.add(peaks, name='data', color=(255,0,0), style='triangle')
		fac.add([(1363.56, 1417.56, 20000,'TEST'),(1100, 1200, 1000, 'TEST')], style='label.spline.bottom', name='spline', color=(0,0,0))
		fac.add([(1363.56, 1417.56, 20000,'TEST'),(1100, 1200, 1000, 'TEST')], style='label.linear.bottom', name='linear', color=(255,0,0))
		fac.add([(1363.56, 1417.56, 20000,'TEST'),(1100, 1200, 1000, 'TEST')], style='label.sticks', name='linear', color=(255,0,0))
		fac.add([(1363.56, 1417.56, 20000,'TEST'),(1100, 1200, 1000, 'TEST')], style='label.triangle', name='linear', color=(255,0,0))
		count += 1
	else:
		count += 1


fac.info()
fac.save(filename='filenameTest')
data = fac.get_json()
