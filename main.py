import argparse
import chromium,firefox,ie,wifi

def dump_all():
	print """                                                                                
                                                                                
                                                                                
    ***        *       **       *     *    *   *      ***      ***      ***     
    *  *      **      *  *    *       *   **   *     *   *     *  *     *   *   
    *  **     ***     *       *       **  **   *    *    **    *   *    *    *  
    *  **     * *     **      **       *  ***  *    *     *    *  *     *    *  
    *  *     *  *       **      **     * ** * *     *     *    ****     *    *  
    *        *****       **      **    * *  * *     *     *    *  *     *    *  
    *       **   *       **       *     **  ***     *    **    *   *    *    *  
    *       *    **   *  *    ** *      **   *       ** **     *   *    *  **   
                                                                                
                                                                                
                                                                                
                                                                                
"""
	ie.dump_ie()
	chromium.dump_browsers()
	firefox.dump_firefox()
	wifi.dump_wifi()
	
if __name__ == '__main__':
	dump_all()