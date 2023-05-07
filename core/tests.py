from django.test import TestCase
from core.models import TodoListModel
from core.forms import TarefasForm, TarefasModelForm
from datetime import datetime

class TarefasTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_index(self):
        self.assertTemplateUsed(self.resp, 'index.html')

class CadastroTarefasTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/cadastro/')

    def test_200_response2(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_cadastro(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

class TodoListModelTest(TestCase):
    def setUp(self):
        self.tarefas= 'Pescar'
        self.mes = 6
        self.dia = 16
        self.cadastro = TodoListModel(
            nome=self.tarefas,  
            dia=self.dia,
            mes=self.mes,
        )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(TodoListModel.objects.exists())

    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)

    def test_nome_tarefa(self):
        nome = self.cadastro.__dict__.get('nome', '')
        self.assertEqual(nome, self.tarefas)

    def test_dia_tarefa(self):
        dia = self.cadastro.__dict__.get('dia', '')
        self.assertEqual(dia, self.dia)

class TarefasFormTest(TestCase):
    def test_forms_has_fields(self):
        form = TarefasModelForm()
        expected = ['nome', 'dia', 'mes']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome = 'Almoço em família')
        self.assertEqual('ALMOÇO EM FAMÍLIA', form.cleaned_data['nome'])
    
    def make_validated_form(self, **kwargs):
        valid = dict(
        nome='Alomço em família',
        dia=7, 
        mes=5
        )
        data = dict(valid, **kwargs)
        form = TarefasForm(data)
        form.is_valid()
        return form
    
class TarefasFormTest(TestCase):
    def test_forms_has_fields(self):
        form = TarefasModelForm()
        expected = ['nome', 'dia', 'mes']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome = 'Almoço em família')
        self.assertEqual('ALMOÇO EM FAMÍLIA', form.cleaned_data['nome'])
    
    def make_validated_form(self, **kwargs):
        valid = dict(
        nome='Almoço em família',
        dia=7, 
        mes=5
        )
        data = dict(valid, **kwargs)
        form = TarefasForm(data)
        form.is_valid()
        return form