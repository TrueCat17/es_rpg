init:
	$ mods["main"] = "Бесконечное Лето 2D"
	$ auto_exit = False


label main:
	jump day0_start


label update:
	call check_change_location


label check_change_location:
	pass



label on_change_location:
	pass
