Simple Enable: cloud.init()

With params: cloud.init(min_alpha=0.1, max_alpha=0.3)

List of params:
* min_alpha,
* max_alpha,
* min_zoom,
* max_zoom,
* min_speed,
* max_speed,
* max_speed_change,
* max_angle_change,
* specials_chance,
* get_count_for_location.

Function <get_count_for_location> takes 1 argument - RpgLocation (not name of location) and
must return count of clouds on this location.

You can see default values of params in cloud.init (cloud__init)


Images:
* usuals (1.png, 03.png, 24.webp),
* specials (all others: my_spec.png, uv.png, cat.webp).

All images are left-up corner of cloud (1/4 part)

All clouds re-generates on each location change
