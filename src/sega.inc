; Processor       : 68020
; Target assembler: 680x0 Assembler in MRI compatible mode
; This file should be compiled with "as -M"
; ===========================================================================
; Segment type: Pure code
; segment "ROM"
; ROM segment
vectors:        dc.l rand_seed
                dc.l Reset
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Check
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l VBLANK
                dc.l Reserv3F
                dc.l Trap0
                dc.l Trap1
                dc.l Trap2
                dc.l Trap3
                dc.l Trap4
                dc.l Trap5
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
                dc.l Reserv3F
CopyRights:     dc.b 'SEGA MEGA DRIVE (C)SEGA 1991.SEP'
DomesticName:   dc.b 'I LOVE DONALD DUCK GURUZIA OH NOHIHOU           '
OverseasName:   dc.b 'QUACK SHOT STARRING DONALD DUCK                 '
ProductCode:    dc.b 'GM 00004054-01'
Checksum:       dc.w $A4B3
Peripherials:   dc.b $4A,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20
RomStart:       dc.l         0
RomEnd:         dc.l   $13FFFF
RamStart:       dc.l M68K_RAM
RamEnd:         dc.l   $FFFFFF
SramCode:       dc.b $20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20
ModemCode:      dc.b $20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20
Reserved:       dc.b $20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,  0,  4,  0,  0,  0, $F,$FF,$FF,$20,$20,$20,$20,$20,$20,$20,$20
CountryCode:    dc.b $4A,$55,$45,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20,$20
