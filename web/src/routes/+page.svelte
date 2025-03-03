<main>
	<section class="hero">
		<div class="row">
			<hgroup>
				<h1>Найди опытного наставника</h1>
				<p>и определи своё направление</p>
			</hgroup>
			<button
				onclick={() => {
					window.location.href = '/mentors';
				}}>Выбрать ментора</button
			>
		</div>

		<h2>О нас</h2>
		<p>
			MentorMatch - платформа, которая соединяет начинающих специалистов с опытными менторами для
			помощи новичкам найти своё направление, не допускать ошибок, и мы
		</p>
	</section>

	<section class="feaыtures">
		<div class="feature-card">
			<h2>Поможем каждому</h2>
			<p>
				На нашем сайте вы найдёте помощь по любому вопросу: определиться, куда поступать, как лучше
				готовиться к экзаменам, как выбрать своё направление, как лучше искать работу, ведь мы
				гордимся своими
			</p>
		</div>
		<div class="feature-cards">
			<h2>Специалистами</h2>
			<div class="landing-cards">
				<div>80%</div>

				<div>100%</div>

				<div>Все</div>
			</div>

			<div class="feature-card">
				<h3>Выбери ментора</h3>
				<p>
					Найди подходящего наставника в удобном списке менторов. Оставь заявку, после одобрения
					которой с тобой свяжется выбранный ментор.
				</p>
				<div class="mentor-buttons">
					<button
						onclick={() => {
							window.location.href = '/mentors';
						}}>Выбрать ментора</button
					>
					<button
						onclick={() => {
							window.location.href = '/mentors/apply';
						}}>Стать ментором</button
					>
				</div>
			</div>
		</div>
	</section>
	<!--
	<section class="cta">
		<a href="/mentors" class="cta-btn">Найти ментора</a>
	</section> -->
</main>

<style>
	.landing-cards {
		display: flex;
	}

	.row {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
</style>
