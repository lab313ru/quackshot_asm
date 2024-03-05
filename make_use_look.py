import os
from shutil import copyfile


def main():
	bak_name = 'src/ingame_menu/use_look_text_or.inc'
	new_name = 'src/ingame_menu/use_look_text_new.inc'
	orig_name = 'src/ingame_menu/use_look_text.inc'

	if not os.path.exists(bak_name):
		copyfile(orig_name, bak_name)

	copyfile(new_name, orig_name)

	bak_name = 'src/ingame_menu/border_vdp_addr_or.inc'
	new_name = 'src/ingame_menu/border_vdp_addr_new.inc'
	orig_name = 'src/ingame_menu/border_vdp_addr.inc'

	if not os.path.exists(bak_name):
		copyfile(orig_name, bak_name)

	copyfile(new_name, orig_name)

	bak_name = 'src/ingame_menu/print_item_border_or.inc'
	new_name = 'src/ingame_menu/print_item_border_new.inc'
	orig_name = 'src/ingame_menu/print_item_border.inc'

	if not os.path.exists(bak_name):
		copyfile(orig_name, bak_name)

	copyfile(new_name, orig_name)

	bak_name = 'src/ingame_menu/item_icons_addr_or.inc'
	new_name = 'src/ingame_menu/item_icons_addr_new.inc'
	orig_name = 'src/ingame_menu/item_icons_addr.inc'

	if not os.path.exists(bak_name):
		copyfile(orig_name, bak_name)

	copyfile(new_name, orig_name)


if __name__ == '__main__':
	main()
