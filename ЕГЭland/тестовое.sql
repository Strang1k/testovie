
SELECT 
    c.id AS course_id,
    c.name AS course_name,
    s.name AS subject_name,
    ct.name AS course_type,
    c.starts_at::DATE AS course_start_date,
    u.id AS student_id,
    u.last_name AS student_last_name,
    u.updated_at as last_update,
    ci.name AS student_city,
    cu.active AS is_active_student,
    cu.created_at::DATE AS course_signup_date,

    -- Количество месяцев и недель с момента старта курса, месяцы для удобства
    date_diff('month', c.starts_at::DATE, current_date) AS course_duration_months,
    date_diff('week', c.starts_at::DATE, current_date) AS course_duration_weeks,


    -- Количество недель с момента зачисления
    date_diff('week', cu.created_at::DATE, current_date) AS weeks_signup,

    -- Количество выполненых дз
    (SELECT COUNT(*) 
     FROM homework_done hd
     JOIN homework_lessons hl ON hd.homework_id = hl.homework_id
     JOIN lessons l ON hl.lesson_id = l.id
     WHERE hd.user_id = u.id AND l.course_id = c.id) AS completed_homeworks_count

FROM users u
JOIN course_users cu ON u.id = cu.user_id
JOIN courses c ON cu.course_id = c.id
JOIN course_types ct ON c.course_type_id = ct.id
JOIN subjects s ON c.subject_id = s.id
JOIN cities ci ON u.city_id = ci.id

WHERE u.user_role_id = 5                   -- Студенты
AND ct.name IN ('Годовой', 'Годовой 2.0')  -- Годовые курсы в явном виде
AND date_diff('week', c.starts_at::DATE, current_date) BETWEEN 0 AND 48 -- Курс длится от 1 до 12 месяцев, с учетом дальнейшего использованя недель

ORDER BY 
    course_duration_weeks DESC,
    c.id, 
    u.last_name;
