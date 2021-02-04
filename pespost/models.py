from django.db import models

# Create your models here.


class Player(models.Model):
    date_field = models.DateField('リリース日', blank=True, null=True)
    initial = models.IntegerField('初期総合値')
    maximum = models.IntegerField('最大総合値')
    level = models.IntegerField('最大レベル')
    player_style = models.CharField('選手タイプ', max_length=20)
    rarity = models.CharField('レアリティ', max_length=10)
    player_name = models.CharField('選手名', max_length=50)
    country = models.CharField('国名', max_length=30)
    league = models.CharField('所属リーグ', max_length=30)
    club = models.CharField('所属クラブ', max_length=30)
    age = models.IntegerField('年齢')
    height = models.IntegerField('身長')
    body_weight = models.IntegerField('体重')
    dominant_foot = models.CharField('利き足', max_length=2)
    position = models.CharField('ポジション', max_length=4)
    playstyle = models.CharField('プレースタイル', max_length=30)
    player_image = models.ImageField(upload_to='')

    def __str__(self):
        return self.player_name


class Ability(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    offense_sense = models.IntegerField('OFセンス')
    ball_control = models.IntegerField('ボールコントロール')
    dribble = models.IntegerField('ドリブル')
    ball_keep = models.IntegerField('ボールキープ')
    grander_pass = models.IntegerField('グランダーパス')
    fly_pass = models.IntegerField('フライパス')
    determining_power = models.IntegerField('決定力')
    heading = models.IntegerField('ヘディング')
    place_kick = models.IntegerField('プレースキック')
    curve = models.IntegerField('カーブ')
    speed = models.IntegerField('スピード')
    instantaneous_power = models.IntegerField('瞬発力')
    kick_power = models.IntegerField('キック力')
    jumping = models.IntegerField('ジャンプ')
    physical_contact = models.IntegerField('フィジカルコンタクト')
    body_control = models.IntegerField('ボディコントロール')
    physical_fitness = models.IntegerField('体力')
    defense_sense = models.IntegerField('ディフェンスセンス')
    take_the_ball = models.IntegerField('ボール奪取')
    aggressiveness = models.IntegerField('アグレッシブネス')
    gksense = models.IntegerField('GKセンス')
    catching = models.IntegerField('キャッチング')
    clearing = models.IntegerField('クリアリング')
    cobraging = models.IntegerField('コブラシング')
    deflectiveing = models.IntegerField('ディフレクティング')
    reverse_foot_frequency = models.IntegerField('逆足頻度')
    reverse_foot_accuracy = models.IntegerField('逆足精度')
    condition_stability = models.IntegerField('コンディション安定度')
    injury_resistance = models.IntegerField('ケガ耐性')


class Skill(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    player_skill = models.CharField('スキル入力', max_length=20, blank=True)


class Formation(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    formation_images = models.ImageField(upload_to='')
