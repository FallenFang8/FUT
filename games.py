import window as win
import button_func as func





############################################################################
#                                                                          #
#                                Tic Tac Toe                               #
#                                                                          #
############################################################################
def tic_tac_toe(app):
    frame = win.alt_create_page(app, "tic_tac_toe_page", "Tic Tac Toe - Coming Soon", back_page="games_page")
    
    
    app.show_page("tic_tac_toe_page")