
import sys
import time

dirPath = './copyleaks'
if dirPath not in sys.path:
    sys.path.insert(0, dirPath)

from copyleakscloud import CopyleaksCloud
from processoptions import ProcessOptions
from product import Product
#    cloud = CopyleaksCloud(Product.Education, 'jiwitesh05nov@gmail.com', 'EBA75E01-5D1A-423E-A237-476C786A1124')


class plagiarism:

    def __init__(self, text, email, key):
        self.text = text
        self.email = email
        self.key = key

    def plag(self):
        cloud = CopyleaksCloud(Product.Education, self.email, self.key)
        #options = ProcessOptions()
        process = cloud.createByText(self.text)

        iscompleted = False
        while not iscompleted:
            # Get process status
            [iscompleted, percents] = process.isCompleted()
            print('%s%s%s%%' % ('#' * int(percents / 2), "-" * (50 - int(percents / 2)), percents))
            if not iscompleted:
                time.sleep(2)

            print("Process Finished!")

            # Get the scan results
        results = process.getResults()
        print('\nFound %s results...' % (len(results)))
        for result in results:
            print('')
            print('------------------------------------------------')
            return result


#check = plagiarism(r"Avul Pakir Jainulabdeen Abdul Kalam  15 October 1931 27 July 2015) was an aerospace scientist who served as the 11th President of India from 2002 to 2007. He was born and raised in Rameswaram, Tamil Nadu and studied physics and aerospace engineering. He spent the next four decades as a scientist and science administrator, mainly at the Defence Research and Development Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's civilian space programme and military missile development efforts.", 'jiwitesh05nov@gmail.com' , 'EBA75E01-5D1A-423E-A237-476C786A1124')
#result = check.plag()
#print(result)