import sys
import logging

# error details are present in sys 
def error_message_details(error,error_detail:sys):
    # exc_info function it will give all the details about the error hence we do not need the info about exc_type,exc_value so we kept underscore
    # we only need exc_trackback
    # trackback has the info about at what point error occured
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message= "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)

    )
    return error_message
class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_messsage=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_messsage


