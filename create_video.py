
from flux import VideoEditor, TextOverlay, Transition, ColorEffect, MusicTrack, SlowMotion

# Инициализация проекта
editor = VideoEditor(width=1080, height=1920, fps=30)

# === Введение (0:00–0:05) ===
# Добавляем лого
intro_logo = editor.add_clip("Лого.JPG", start=0, duration=2)

# Текст на экране
intro_text = TextOverlay(
    text="Премиум стрижка от международного стилиста",
    position=("center", "top"),
    font_size=36,
    color="#D4AF37",  # Золотой цвет
    fade_in=1
)
editor.add_overlay(intro_text, start=0)

# Плавный fade-in логотипа
editor.add_transition(Transition(type="fade", duration=1), clip=intro_logo)

# === Кадр "до стрижки" (0:05–0:10) ===
before_clip = editor.add_clip("IMG_0399.jpeg", start=5, duration=5)

# Добавляем текст "До процедуры"
before_text = TextOverlay(
    text="До процедуры",
    position=("center", "bottom"),
    font_size=28,
    color="#FFFFFF",  # Чистый белый
    fade_in=1
)
editor.add_overlay(before_text, start=5)

# Переход между кадрами
editor.add_transition(Transition(type="dissolve", duration=1), clip=before_clip)

# === Процесс стрижки (0:10–0:20) ===
process_clip = editor.add_clip("IMG_0407.mov", start=10, duration=10)

# Текст для процесса
process_text = TextOverlay(
    text="Процесс премиальной стрижки",
    position=("center", "top"),
    font_size=28,
    color="#8A8A8A",  # Светло-серый
    fade_in=1
)
editor.add_overlay(process_text, start=10)

# Эффект: Замедление
editor.add_effect(SlowMotion(factor=0.5), clip=process_clip)

# === Кадр "после стрижки" (0:20–0:25) ===
after_clip = editor.add_clip("IMG_0409.jpeg", start=20, duration=5)

# Текст для результата
after_text = TextOverlay(
    text="Идеальная форма и стиль",
    position=("center", "bottom"),
    font_size=28,
    color="#D4AF37",  # Золотой цвет
    fade_in=1
)
editor.add_overlay(after_text, start=20)

# Переход к результату: Мягкий flash
editor.add_transition(Transition(type="flash", duration=0.5), clip=after_clip)

# === Финал (0:25–0:30) ===
final_logo = editor.add_clip("Лого.JPG", start=25, duration=5)

# Призыв к действию
final_text = TextOverlay(
    text="Запишитесь на премиальную стрижку\nМеждународный стилист, премиальный сервис",
    position=("center", "top"),
    font_size=32,
    color="#D4AF37",  # Золотой цвет
    fade_in=1
)
editor.add_overlay(final_text, start=25)

# Добавляем затемнение для завершения
editor.add_transition(Transition(type="fade", duration=1), clip=final_logo)

# === Музыка ===
background_music = MusicTrack("background_music.mp3", volume=0.5)
editor.add_music(background_music)

# Экспорт видео
editor.render(output="premium_haircut_video.mp4")
