from django import forms


class VcfForm(forms.Form):

    vcf = forms.CharField(label='vcf', widget=forms.CharField)


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Selecione um arquivo (.VCF)'
    )
