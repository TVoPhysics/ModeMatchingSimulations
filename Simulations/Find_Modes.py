import trace_mode
import pykat

def find_all(kat_findmode, q_sqz_x, q_sqz_y):
        #### Turn off all the cav commands except SRCY to extract the eigenmode at the BS
        [srcx,srcy] = trace_mode.from_cav_to_BS(kat_findmode,'cavSRY')

        #### Turn off all the cav commands except XARM to extract the eigenmode at the BS
        [ARMx,ARMy] = trace_mode.from_cav_to_BS(kat_findmode,'cavXARM')

        #### Turn off all the cav commands except OMC to extract the eigenmode at the BS
        [OMCx,OMCy] = trace_mode.from_cav_to_BS(kat_findmode,'cavOMC')

        #### Turn off all the cav commands except FC to extract the eigenmode at the BS
        [FCx,FCy] = trace_mode.from_cav_to_BS(kat_findmode,'cavFC')

        #### Get the sqz mode at the BS, this is more difficult because in Finesse, the sqzer is not a cavity.
        [q_sqz_BS_x,q_sqz_BS_y] = trace_mode.get_sqz_mode_BS(
                kat_findmode,q_sqz_x,q_sqz_y)

        strings = ['SRCx', 'SRCy',
                  'ARMx', 'ARMy',
                  'OMCx', 'OMCy',
                  'FCx', 'FCy',
                  'q_sqz_BS_x','q_sqz_BS_y']
        
        values = [srcx,srcy,
                 ARMx,ARMy,
                 OMCx,OMCy,
                 FCx,FCy,
                 q_sqz_BS_x,q_sqz_BS_y]
        
        strings_values = zip(strings, values)
    
        dictionary = {}
        for strings, values in strings_values:
            dictionary[strings] = values
        
        return dictionary
