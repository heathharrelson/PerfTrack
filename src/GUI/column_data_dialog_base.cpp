#include "column_data_dialog_base.h"

#include <qvariant.h>

#include "column_data_dialog_base.moc"
/*
 *  Constructs a ColumnDataDialogBase as a child of 'parent', with the
 *  name 'name' and widget flags set to 'f'.
 *
 *  The dialog will by default be modeless, unless you set 'modal' to
 *  true to construct a modal dialog.
 */
ColumnDataDialogBase::ColumnDataDialogBase(QWidget* parent, const char* name, bool modal, Qt::WindowFlags fl)
    : QDialog(parent, name, modal, fl)
{
    setupUi(this);

}

/*
 *  Destroys the object and frees any allocated resources
 */
ColumnDataDialogBase::~ColumnDataDialogBase()
{
    // no need to delete child widgets, Qt does it all for us
}

/*
 *  Sets the strings of the subwidgets using the current
 *  language.
 */
void ColumnDataDialogBase::languageChange()
{
    retranslateUi(this);
}

