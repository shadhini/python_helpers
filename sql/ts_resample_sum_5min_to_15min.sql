select max(`time`) as time, sum(`value`) as value from `data` where `id`=%s and `time` >= %s and `time` <= %s
group by floor(((to_seconds(time)/60)-1)/15);