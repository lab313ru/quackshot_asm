print_item_upper_border1:
                move.l  #$80358036,(a6)
                move.l  #$80368036,(a6)
                move.l  #$80368036,(a6)
; End of function print_item_upper_border1
print_item_upper_border2:
                move.l  #$80368036,(a6)
                move.l  #$80368835,(a6)
                rts
; End of function print_item_upper_border2
print_item_lower_border1:
                move.l  d0,(a5)
                move.l  #$90359036,(a6)
                move.l  #$90369036,(a6)
                move.l  #$90369036,(a6)
print_item_lower_border2:
                move.l  #$90369036,(a6)
                move.l  #$90369835,(a6)
                move    #$2500,sr
                rts
; End of function print_item_lower_border1
